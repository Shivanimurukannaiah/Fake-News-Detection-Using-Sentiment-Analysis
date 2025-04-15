
def predict_news(model, text):
    prediction = model.predict([text])[0]
    prob = model.predict_proba([text])[0].max()
    return prediction, round(prob * 100, 2)
