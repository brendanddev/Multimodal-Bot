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
    print(f"Sentiment scores for '{utterance}': {sentiment_score}")
    
    # Get overall (compound)
    if sentiment_score['compound'] > 0.2:
        sentiment = "positive"
    elif sentiment_score['compound'] < -0.2:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    print(f"Sentiment detected by NLTK: {sentiment}")

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
    print(f"Emotion detected by TextBlob: {emotion}")
    
    return sentiment, emotion


if __name__ == "__main__":
    test_cases = [
        "I love this place!", 
        "I hate waiting.",  
        "It's okay, not great but not bad.", 
        "This is the worst thing ever.",  
        "Wow! This is amazing!!! 😍", # emoji?
        "Meh, I don't know how I feel about this." 
    ]
    
    print("\nRunning sentiment analysis on test cases...\n")
    for test in test_cases:
        print(f"Analyzing sentiment for: {test}")
        result = analyze_sentiment(test)
        print(f"Sentiment: {result}\n")