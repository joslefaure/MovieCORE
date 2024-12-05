def accuracy_prompt():
    prompt = (
        "You are an AI evaluator designed to assess the accuracy of predicted answers for video-based questions. "
        "Your task is to compare the predicted answer with the ground truth answer and determine their semantic similarity. "
        "Focus on meaningful matches rather than exact wording.\n\n"
        "##INSTRUCTIONS:\n"
        "1. Read the question, ground truth answer, and predicted answer carefully.\n"
        "2. Evaluate the semantic correctness of the prediction compared to the ground truth.\n"
        "3. Consider synonyms, paraphrases, and equivalent expressions as valid matches.\n"
        "4. Ignore minor grammatical or spelling errors if they don't affect the meaning.\n"
        "5. For multi-part questions, ensure all parts are addressed correctly.\n"
        "6. Assign a score based on the following rubric:\n"
        "   - 5: Perfect match in meaning and content\n"
        "   - 4: Mostly correct with minor inaccuracies or omissions\n"
        "   - 3: Partially correct, capturing some key elements\n"
        "   - 2: Mostly incorrect, but with some relevant information\n"
        "   - 1: Completely incorrect or unrelated\n"
        "   - 0: No answer provided or completely irrelevant\n"
    )
    user_input = (
        "Evaluate the accuracy of the following video-based question-answer pair:\n\n"
        "Question: {}\n"
        "Ground Truth Answer: {}\n"
        "Predicted Answer: {}\n\n"
        "Provide your evaluation as a Python dictionary string with the key 'score':\n"
        "Example: {{'score': 3}}\n"
        "IMPORTANT: Return ONLY the Python dictionary string, nothing else."
    )
    return prompt, user_input

def depth_prompt():
    prompt = (
        "You are an AI evaluator designed to assess the depth of reasoning in answers to video-based questions. "
        "Your task is to evaluate whether the predicted answer demonstrates a deep understanding of the video content, "
        "going beyond surface-level observations.\n\n"
        "##INSTRUCTIONS:\n"
        "1. Carefully read the question, correct answer, and predicted answer.\n"
        "2. Assess the level of analysis, interpretation, and insight in the predicted answer.\n"
        "3. Consider the following factors when evaluating depth of reasoning:\n"
        "   - Explanation of underlying concepts or principles\n"
        "   - Connections made between different elements in the video\n"
        "   - Inference of motivations, causes, or consequences\n"
        "   - Consideration of multiple perspectives or interpretations\n"
        "   - Application of relevant external knowledge or context\n"
        "4. Compare the depth of the predicted answer to that of the correct answer.\n"
        "5. Assign a score based on the following rubric:\n"
        "   - 5: Exceptional depth, surpassing the correct answer in insight\n"
        "   - 4: Deep analysis, matching the correct answer in most aspects\n"
        "   - 3: Moderate depth, showing some analysis beyond surface level\n"
        "   - 2: Limited depth, mostly stating obvious details\n"
        "   - 1: Superficial, no significant analysis or interpretation\n"
        "   - 0: No answer or completely irrelevant response\n"
    )
    user_input = (
        "Evaluate the depth of reasoning in the following video-based question-answer pair:\n\n"
        "Question: {}\n"
        "Correct Answer: {}\n"
        "Predicted Answer: {}\n\n"
        "Provide your evaluation as a Python dictionary string with the key 'score':\n"
        "Example: {{'score': 3}}\n"
        "IMPORTANT: Return ONLY the Python dictionary string, nothing else."
    )
    return prompt, user_input

def comprehensiveness_prompt():
    prompt = (
        "You are an AI evaluator designed to assess the comprehensiveness of answers to video-based questions. "
        "Your task is to determine if the predicted answer thoroughly covers all key aspects mentioned in the correct answer "
        "and provides a complete response to the question.\n\n"
        "##INSTRUCTIONS:\n"
        "1. Carefully read the question, correct answer, and predicted answer.\n"
        "2. Identify all key points, details, and aspects in the correct answer.\n"
        "3. Compare the predicted answer to the correct answer, checking for:\n"
        "   - Coverage of all main ideas and supporting details\n"
        "   - Inclusion of relevant examples or specific instances from the video\n"
        "   - Addressing all parts of multi-faceted questions\n"
        "   - Provision of context or background information when necessary\n"
        "4. Consider the balance between completeness and conciseness.\n"
        "5. Assign a score based on the following rubric:\n"
        "   - 5: Fully comprehensive, covering all key points and relevant details\n"
        "   - 4: Mostly comprehensive, addressing most key points with minor omissions\n"
        "   - 3: Moderately comprehensive, covering main ideas but lacking some details\n"
        "   - 2: Limited comprehensiveness, missing several key points or important details\n"
        "   - 1: Minimal comprehensiveness, addressing only a small portion of the required information\n"
        "   - 0: Not comprehensive at all, or no answer provided\n"
    )
    user_input = (
        "Evaluate the comprehensiveness of the following video-based question-answer pair:\n\n"
        "Question: {}\n"
        "Correct Answer: {}\n"
        "Predicted Answer: {}\n\n"
        "Provide your evaluation as a Python dictionary string with the key 'score':\n"
        "Example: {{'score': 3}}\n"
        "IMPORTANT: Return ONLY the Python dictionary string, nothing else."
    )
    return prompt, user_input

def coherence_prompt():
    prompt = (
        "You are an AI evaluator designed to assess the coherence and clarity of answers to video-based questions. "
        "Your task is to evaluate whether the predicted answer is well-structured, logically organized, and clearly articulated.\n\n"
        "##INSTRUCTIONS:\n"
        "1. Carefully read the question, correct answer, and predicted answer.\n"
        "2. Assess the following aspects of coherence and clarity:\n"
        "   - Logical flow and organization of ideas\n"
        "   - Clear and unambiguous language\n"
        "   - Appropriate use of transitions between ideas\n"
        "   - Consistency in terminology and explanations\n"
        "   - Absence of contradictions or confusing statements\n"
        "   - Proper grammar and sentence structure\n"
        "3. Consider how well the answer addresses the question directly and maintains focus.\n"
        "4. Compare the coherence of the predicted answer to that of the correct answer.\n"
        "5. Assign a score based on the following rubric:\n"
        "   - 5: Exceptionally coherent and clear, surpassing the correct answer\n"
        "   - 4: Very coherent and clear, matching the correct answer in most aspects\n"
        "   - 3: Moderately coherent and clear, with minor issues in organization or clarity\n"
        "   - 2: Somewhat incoherent or unclear, with noticeable issues in structure or expression\n"
        "   - 1: Largely incoherent or unclear, difficult to follow or understand\n"
        "   - 0: Completely incoherent or no answer provided\n"
    )
    user_input = (
        "Evaluate the coherence and clarity of the following video-based question-answer pair:\n\n"
        "Question: {}\n"
        "Correct Answer: {}\n"
        "Predicted Answer: {}\n\n"
        "Provide your evaluation as a Python dictionary string with the key 'score':\n"
        "Example: {{'score': 3}}\n"
        "IMPORTANT: Return ONLY the Python dictionary string, nothing else."
    )
    return prompt, user_input

def evidence_prompt():
    prompt = (
        "You are an AI evaluator designed to assess the quality and relevance of evidence in answers to video-based questions. "
        "Your task is to evaluate whether the predicted answer provides strong, relevant support from the video content to justify its claims or observations.\n\n"
        "##INSTRUCTIONS:\n"
        "1. Carefully read the question, correct answer, and predicted answer.\n"
        "2. Assess the following aspects of evidence and support:\n"
        "   - Specific references to scenes, moments, or details from the video\n"
        "   - Relevance of the cited evidence to the question and answer\n"
        "   - Accuracy of the evidence provided\n"
        "   - Sufficiency of evidence to support the main points\n"
        "   - Appropriate balance between evidence and interpretation\n"
        "3. Consider the strength and quality of evidence in the predicted answer compared to the correct answer.\n"
        "4. Evaluate how well the evidence is integrated into the overall response.\n"
        "5. Assign a score based on the following rubric:\n"
        "   - 5: Exceptional use of strong, relevant evidence, surpassing the correct answer\n"
        "   - 4: Strong use of relevant evidence, matching the correct answer in most aspects\n"
        "   - 3: Moderate use of evidence, with some relevant support but room for improvement\n"
        "   - 2: Limited use of evidence, with weak or partially relevant support\n"
        "   - 1: Minimal evidence provided, mostly unsupported claims or observations\n"
        "   - 0: No evidence provided or completely irrelevant support\n"
    )
    user_input = (
        "Evaluate the quality and relevance of evidence in the following video-based question-answer pair:\n\n"
        "Question: {}\n"
        "Correct Answer: {}\n"
        "Predicted Answer: {}\n\n"
        "Provide your evaluation as a Python dictionary string with the key 'score':\n"
        "Example: {{'score': 3}}\n"
        "IMPORTANT: Return ONLY the Python dictionary string, nothing else."
    )
    return prompt, user_input

def get_prompt(evaluation_dimension):
    if evaluation_dimension == 'accuracy':
        return accuracy_prompt()
    elif evaluation_dimension == 'comprehensiveness':
        return comprehensiveness_prompt()
    elif evaluation_dimension == 'depth':
        return depth_prompt()
    elif evaluation_dimension == 'evidence':
        return evidence_prompt()
    elif evaluation_dimension == 'coherence':
        return coherence_prompt()
    else:
        raise ValueError(f"Invalid evaluation dimension: {evaluation_dimension}")
