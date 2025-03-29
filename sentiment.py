
"""
Sentiment Analysis using TextBlob's Statistical Sentiment Analysis
Brendan Dileo
"""
from textblob import TextBlob

def analyze_sentiment(utterance):
    polarity = TextBlob(utterance).sentiment.polarity
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    return "neutral"

