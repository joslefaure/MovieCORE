
<div align="center">
  <img src="assets/moviecore_icon.png" alt="MovieCORE Icon" width="150"/>
  
  # MovieCORE
  
  **A Video Question Answering Dataset for Probing Deeper Cognitive Understanding of Movie Content**
  
  [![arXiv](https://img.shields.io/badge/arXiv-2508.19026-b31b1b.svg)](https://arxiv.org/abs/2508.19026)
  [![Dataset](https://img.shields.io/badge/🤗%20Dataset-HuggingFace-yellow.svg)](https://huggingface.co/datasets/MovieCORE/MovieCORE)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
  
  ![MovieCore Dataset](assets/poster_teaser.png)
</div>

## 📖 Overview

MovieCORE is a comprehensive video question answering (VQA) dataset specifically designed to evaluate and probe deeper cognitive understanding of movie content. Unlike traditional VQA datasets that focus on surface-level visual understanding, MovieCORE challenges models to demonstrate sophisticated reasoning about narrative structures, character development, thematic elements, and complex temporal relationships within cinematic content.

## 🗂️ Data Preparation

The MovieCORE dataset builds upon video content from MovieChat. To get started:

### Video Data
Download the video files from MovieChat's HuggingFace repositories:
- **Training Data**: [MovieChat-1K Train](https://huggingface.co/datasets/Enxin/MovieChat-1K_train)
- **Test Data**: [MovieChat-1K Test](https://huggingface.co/datasets/Enxin/MovieChat-1K-test)

### Annotations
Access our carefully curated annotations on HuggingFace:
- **MovieCORE Annotations**: [🤗 HuggingFace Dataset](https://huggingface.co/datasets/MovieCORE/MovieCORE/tree/main)

Extract and organize the data according to your model's requirements, then use our annotations for evaluation.

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/joslefaure/MovieCORE.git
cd MovieCORE
pip install -r requirements.txt  # Install dependencies
```

## 🎯 Baselines
*Coming soon - We will provide baseline implementations and results for popular VQA models.*

## 📊 Evaluation Dimensions

MovieCORE employs a comprehensive multi-dimensional evaluation framework to assess model performance across different aspects of cognitive understanding:

| Dimension | Description |
|-----------|-------------|
| **🎯 Accuracy** | Measures semantic similarity between predicted and ground truth answers |
| **📋 Comprehensiveness** | Assesses coverage of all key aspects mentioned in the ground truth |
| **🧠 Depth** | Evaluates level of reasoning and insight demonstrated in predictions |
| **🔍 Evidence** | Checks quality and relevance of supporting evidence provided |
| **🔗 Coherence** | Measures logical flow, organization, and clarity of responses |

Each dimension provides unique insights into different cognitive capabilities required for deep video understanding.

## 💻 Usage

### Evaluation Script

Evaluate your model's performance on MovieCORE using our evaluation script:

```bash
export OPENAI_API_KEY='your_openai_api_key'
python evaluate_moviecore.py --pred_path path/to/your/predictions.json
```

### 📝 Input Format

Your predictions should follow this JSON structure:

```json
{
    "video_1.mp4": [
        {
            "question": "How does the video depict the unique adaptations of the species in the Sahara Desert, and what roles do these species play in their ecosystem?",
            "answer": "The ground truth answer.",
            "pred": "Your model's prediction.",
            "classification": "the question classification"
        },
        {
            "question": "The second question for video 1?",
            "answer": "The ground truth answer.",
            "pred": "Your model's prediction.",
            "classification": "the question classification"
        }
    ],
    "video_2.mp4": [
        {
            "question": "The only question for video 2",
            "answer": "The ground truth answer.",
            "pred": "Your model's prediction.",
            "classification": "the question classification"
        }
    ]
}
```

### 📈 Output

The evaluation script provides:
- Overall scores across all dimensions
- Classification-specific performance metrics
- Detailed breakdowns for comprehensive analysis

## 📚 Citation

If you use MovieCORE in your research, please cite our paper:

```bibtex
@misc{faure2025moviecorecognitivereasoningmovies,
      title={MovieCORE: COgnitive REasoning in Movies}, 
      author={Gueter Josmy Faure and Min-Hung Chen and Jia-Fong Yeh and Ying Cheng and Hung-Ting Su and Yung-Hao Tang and Shang-Hong Lai and Winston H. Hsu},
      year={2025},
      eprint={2508.19026},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2508.19026}, 
}
```

## 🤝 Contributing

We welcome contributions to MovieCORE! Please feel free to:
- Report issues or bugs
- Suggest improvements or new features
- Submit baseline implementations
- Provide feedback on the evaluation framework

## 📄 License

This dataset is provided under the MIT License. See [LICENSE](LICENSE) for more details.

---

<div align="center">
  <p>🎬 <strong>Advancing Video Understanding Through Cognitive Evaluation</strong> 🎬</p>
  
  **[📖 Paper](https://arxiv.org/abs/2508.19026v1) | [🤗 Dataset](https://huggingface.co/datasets/MovieCORE/MovieCORE) | [💻 Code](https://github.com/joslefaure/MovieCORE)**
</div>