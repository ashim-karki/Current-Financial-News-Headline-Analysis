# Current-Financial-News-Headline-Analysis
This BERT cased model was fine-tuned on the Kaggle dataset using Huggingface library and Beautifulsoup was used for scraping google news for relevant news headlines.

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
1. ```pip install -r requirements.txt

2. run **notebooks/training.ipynb** and the trained model will be stored in **models** folder.

3. ```streamlit run sentiment.py

### Output

1. Enter the number of news headlines to scrape from google news along with the relevant topic:
<img src="https://github.com/user-attachments/assets/8d34cfe0-82db-4d5d-8272-19f071374cf4" alt="Screenshot" width="400"/>

3. Press Submit after which scraping and sentiment analysis will begin:
![Screenshot 2024-12-15 at 9 03 55 AM](https://github.com/user-attachments/assets/62768433-7d3e-4a62-9af8-2792bdd7d845)

4. Evaluated news headlines can be viewed as:
![Screenshot 2024-12-15 at 9 04 54 AM](https://github.com/user-attachments/assets/65004c3c-1cfd-4afa-8449-f27f33bf7b68)
![Screenshot 2024-12-15 at 9 05 13 AM](https://github.com/user-attachments/assets/f1e4448b-103f-4de6-bcbb-dbba752104ad)


