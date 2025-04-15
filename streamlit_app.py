
import streamlit as st
from src.data_loader import load_news_data
from src.preprocessor import clean_text
from src.sentiment_model import build_model, train_model
from src.predictor import predict_news

st.title("📰 Fake News Detection App")

df = load_news_data("data/news_sample.csv")
df['clean_text'] = df['text'].apply(clean_text)

model = build_model()
model = train_model(model, df['clean_text'], df['label'])

user_input = st.text_area("Enter news article text here:")
if st.button("Check if Fake"):
    cleaned = clean_text(user_input)
    label, confidence = predict_news(model, cleaned)
    st.write(f"### Prediction: `{label.upper()}`")
    st.write(f"### Confidence: {confidence}%")
