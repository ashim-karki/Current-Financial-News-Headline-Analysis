import pandas as pd
import streamlit as st
import requests
from bs4 import BeautifulSoup
import torch
from transformers import BertTokenizer, BertForSequenceClassification
import altair as alt

st.set_page_config(layout="wide")

st.title("Current Financial News Sentiment Analysis")

number_of_headlines = int(st.text_input("Enter the number of news headlines to analyze.", "10"))
query = st.text_input("Enter the news headline to analyze.", "USA Economy")

if(st.button('Submit')):
    st.success(f"The number of news headlines to extract: {number_of_headlines}")
    st.success(f"The topic to be analyzed: {query}")

    st.write("Fetching news headlines...")

    # This function encodes special characters in the query string to make it URL-safe
    def encode_special_characters(text):
        encoded_text = ''
        special_characters = {'&': '%26', '=': '%3D', '+': '%2B', ' ': '%20'}  # Add more special characters as needed
        for char in text.lower():
            encoded_text += special_characters.get(char, char)
        return encoded_text

    # query2 is the URL-safe version of the query string
    query2 = encode_special_characters(query)
    url = f"https://news.google.com/search?q={query2}&hl=en-US&gl=US&ceid=US%3Aen&sortby=date"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('article')[:number_of_headlines] # Get the first selected articles
    base_url = "https://news.google.com"
    links = [base_url + article.find('a')['href'][1:] for article in articles]  # Remove the leading '.' and append to base_url

    # Follow the redirect links to get the actual news website URLs
    actual_links = []
    for link in links:
        response = requests.get(link)
        actual_links.append(response.url)

    news_text = [article.get_text(separator='\n') for article in articles]
    news_text_split = [text.split('\n') for text in news_text]

    st.success("News headlines fetched successfully!")

    st.write("Analyzing news headlines...")

    model = BertForSequenceClassification.from_pretrained("models/")
    tokenizer = BertTokenizer.from_pretrained("models/")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model.to(device)
    model.eval()
    sentiments = []

    for text in news_text_split:
        inputs = tokenizer(text[2], return_tensors="pt", padding=True, truncation=True, max_length=128)
        inputs = {key: val.to(device) for key, val in inputs.items()}
        outputs = model(**inputs)
        logits = outputs.logits
        prediction = torch.argmax(logits, dim=1).item()
        sentiment_re_mapping = {0 : 'positive', 1 : 'negative', 2 : 'neutral'}
        sentiments.append(sentiment_re_mapping[prediction])

    news_df = pd.DataFrame({
        'Title': [text[2] for text in news_text_split],
        'Source': [text[0] for text in news_text_split],
        'Sentiment': sentiments,
        'Time': [text[3] if len(text) > 3 else 'Missing' for text in news_text_split],
        'Author': [text[4].split('By ')[-1] if len(text) > 4 else 'Missing' for text in news_text_split],
        'Link': actual_links
    })

    st.success("News headlines analyzed successfully!")

    st.write(news_df)

    # Display sentiment counts as a bar chart using Altair
    sentiment_counts = news_df["Sentiment"].value_counts().reset_index()
    sentiment_counts.columns = ['Sentiment', 'Count']

    chart = alt.Chart(sentiment_counts).mark_bar().encode(
        x=alt.X('Sentiment', sort=None),
        y='Count',
        color='Sentiment'
    ).properties(
        width=600,
        height=400
    )

    st.write(news_df["Sentiment"].value_counts())
    st.altair_chart(chart)
