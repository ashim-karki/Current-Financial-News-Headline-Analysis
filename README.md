# Current-Financial-News-Headline-Analysis
This BERT cased model was fine-tuned on the Kaggle dataset using Huggingface library.

Dataset: [Sentiment Analysis for Financial News](https://www.kaggle.com/datasets/ankurzing/sentiment-analysis-for-financial-news)

### Model's evaluation:
- Accuracy: 0.8639175257731959
- Precision: 0.8663562452727861
- Recall: 0.8639175257731959
- F1 Score: 0.8646045145985588

**Classification Report**
| Class       | Precision | Recall | F1-Score | Support |
|-------------|-----------|--------|----------|---------|
| Positive    | 0.80      | 0.86   | 0.83     | 146     |
| Negative    | 0.86      | 0.86   | 0.86     | 58      |
| Neutral     | 0.90      | 0.87   | 0.89     | 281     |
| **Accuracy**|           |        | 0.86     | 485     |
| **Macro Avg** | 0.85    | 0.86   | 0.86     | 485     |
| **Weighted Avg** | 0.87 | 0.86   | 0.86     | 485     |

### Installation:
1. ```bash
pip install -r requirements.txt

2. run notebooks/training.ipynb

3. ```bash
streamlit run sentiment.py   

