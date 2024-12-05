import multiprocessing
import openai
import json
import os
from tqdm import tqdm
import time
from openai.error import RateLimitError, Timeout, APIError
import ast
from evaluation_prompts import get_prompt

api_key = os.getenv("OPENAI_API_KEY")

evaluation_dimensions = ['accuracy', 'comprehensiveness', 'depth', 'evidence', 'coherence']

def evaluate_qa_pair(data, retries=3, delay=10):
    question, answer, pred = data['question'], data['answer'], data['pred']
    classification = data['classification']
    results = {}
    for evaluation_dimension in evaluation_dimensions:
        prompt, user_input = get_prompt(evaluation_dimension)
        user_input = user_input.format(question, answer, pred)

        for attempt in range(retries):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4o-mini-2024-07-18",
                    messages=[
                        {"role": "system", "content": prompt},
                        {"role": "user", "content": user_input},
                    ],
                    timeout=30
                )
                response_message = response["choices"][0]["message"]["content"]
                response_message = response_message.replace("```python", "").replace("```", "").strip()
                results[evaluation_dimension] = ast.literal_eval(response_message)
                break
            except (RateLimitError, APIError) as e:
                print(f"Rate limit or API error encountered: {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
            except Timeout as e:
                print(f"Request timed out: {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
            except Exception as e:
                print(f"Unexpected error: {e}")
                break
    return {'results': results, 'classification': classification}

def worker(data):
    return evaluate_qa_pair(data)

def calculate_scores(results_list):
    # Initialize dictionaries to store aggregated scores
    classification_scores = {}
    overall_scores = {dim: {'total': 0, 'count': 0} for dim in evaluation_dimensions}
    
    for item in results_list:
        if not item or 'results' not in item:
            continue
            
        # Split classifications and strip whitespace
        classifications = [c.strip() for c in item['classification'].split(',')]
        
        # Process each classification separately
        for classification in classifications:
            if classification not in classification_scores:
                classification_scores[classification] = {
                    dim: {'total': 0, 'count': 0} for dim in evaluation_dimensions
                }
            
            # Add scores for each dimension
            for dimension, result in item['results'].items():
                try:
                    score = result['score']
                    # Add to classification-specific scores
                    classification_scores[classification][dimension]['total'] += score
                    classification_scores[classification][dimension]['count'] += 1
                    # Add to overall scores
                    overall_scores[dimension]['total'] += score
                    overall_scores[dimension]['count'] += 1
                except:
                    continue

    # Calculate averages for each classification and dimension
    final_results = {'overall': {}, 'by_classification': {}}
    
    # Calculate overall averages for each dimension
    final_results['overall'] = {
        dim: overall_scores[dim]['total'] / overall_scores[dim]['count']
        if overall_scores[dim]['count'] > 0 else 0
        for dim in evaluation_dimensions
    }
    
    # Calculate overall average across all dimensions
    all_dimension_scores = [score for score in final_results['overall'].values()]
    final_results['overall']['average_across_dimensions'] = (
        sum(all_dimension_scores) / len(all_dimension_scores)
        if all_dimension_scores else 0
    )
    
    # Calculate averages for each classification
    for classification in classification_scores:
        # Calculate averages for each dimension
        dimension_scores = {
            dim: classification_scores[classification][dim]['total'] / 
                 classification_scores[classification][dim]['count']
            if classification_scores[classification][dim]['count'] > 0 else 0
            for dim in evaluation_dimensions
        }
        
        # Calculate average across all dimensions for this classification
        avg_across_dimensions = (
            sum(dimension_scores.values()) / len(dimension_scores)
            if dimension_scores else 0
        )
        
        # Store both individual dimension scores and the overall average
        final_results["by_classification"][classification] = dimension_scores
        final_results["by_classification"][classification]['average_across_dimensions'] = avg_across_dimensions
    
    return final_results

def main(pred_path):
    with open(pred_path, 'r') as pred_file:
        pred_contents = json.load(pred_file)

    data_for_workers = []
    for sample in pred_contents:
        id = sample.split(".")[0]
        qa_list = pred_contents[sample]
        for qa_pair in qa_list:
            question = qa_pair['question']
            if "enhanced_answer" in qa_pair:
                answer = qa_pair['enhanced_answer'][-1]["content"]
            else:
                answer = qa_pair['answer']
            pred = qa_pair['pred'].replace("</s>", "")
            data_for_workers.append({
                "question": question,
                "answer": answer,
                "pred": pred,
                "classification": qa_pair['classification']
            })
        # break

    total_items = len(data_for_workers)
    pool = multiprocessing.Pool(processes=8)

    with tqdm(total=total_items, desc="Processing") as pbar:
        results = []
        for result in pool.imap_unordered(worker, data_for_workers):
            results.append(result)
            pbar.update()

    pool.close()
    pool.join()

    # Calculate scores for overall and by classification
    final_scores = calculate_scores(results)
    return json.dumps(final_scores, indent=4)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Evaluate MovieCore dataset")
    parser.add_argument('--pred_path', type=str, required=True, help='Path to the JSON file containing the predictions')
    args = parser.parse_args()

    res = main(args.pred_path)
    print(res)
