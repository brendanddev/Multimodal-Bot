"""
sentiment.py
https://www.nltk.org/api/nltk.sentiment.SentimentIntensityAnalyzer.html

Brendan Dileo, April 2025
"""

from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

def analyze_sentiment(utterance):
    # init
    sid = SentimentIntensityAnalyzer()

    # Gets the sentiment scores
    sentiment_score = sid.polarity_scores(utterance)
    
    # Get overall (compound)
    if sentiment_score['compound'] > 0.2:
        sentiment = "positive"
    elif sentiment_score['compound'] < -0.2:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    # init
    blob = TextBlob(utterance)
    # Extract sentiment
    blob_sentiment = blob.sentiment.polarity
    # Checks polarity of sentiment to categorize emotion (basic)
    if blob_sentiment > 0.5:
            emotion = "happy"
    elif blob_sentiment < -0.5:
            emotion = "sad"
    else:
            emotion = "neutral"
    
    return sentiment, emotion