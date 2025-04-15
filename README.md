# Fake-News-Detection-Using-Sentiment-Analysis
a model that detects fake news articles by analyzing their sentiment and comparing it to known patterns of misinformation. This project involves natural language processing techniques and contributes to combating the spread of false information.
# 📰 Fake News Detection Using Sentiment Analysis

Use natural language processing (NLP) to detect fake news by analyzing sentiment and content patterns in headlines and articles.

## 🔍 Features
- Sentiment scoring of article text
- TF-IDF + Logistic Regression model for classification
- Streamlit interface for input & prediction
- Built with NLTK, Scikit-learn, Streamlit

## 🚀 Getting Started

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## 📁 Folder Structure

```
Fake-News-Detection/
│
├── app/
│   └── streamlit_app.py
├── data/
│   └── news_sample.csv
├── src/
│   ├── data_loader.py
│   ├── preprocessor.py
│   ├── sentiment_model.py
│   └── predictor.py
├── utils/
│   └── helpers.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## 📸 Sample Output

> "This article has a high negative sentiment and a 92% probability of being fake."

## 🧠 Author

Created by Shivani Murukannaiah | [LinkedIn](www.linkedin.com/in/shivani1405)  
Licensed under MIT.
