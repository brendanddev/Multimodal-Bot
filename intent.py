

from text_processing import clean_utterance
from pattern_matching import heuristic_match
from classify_speech import classify_speech_act
from sentiment import analyze_sentiment
from entities import extract_entities
from statistical import classify_statistical_intent, generate_statistical_response
import random 

def understand(utterance, intents, regex_patterns):
    cleaned_utterance = clean_utterance(utterance)

    # Heuristic approach
    match, pattern_score = heuristic_match(cleaned_utterance, intents, regex_patterns)
    
    # Sentimental Approach
    sentiment = analyze_sentiment(cleaned_utterance)
    sentiment_score = 0
    if sentiment == "positive":
        sentiment_score = 1
    elif sentiment == "negative":
        sentiment_score = -1

    # Speech Act Classification
    speech_act = classify_speech_act(cleaned_utterance)
    speech_act_score = 0
    if speech_act == "question":
        speech_act_score = 2
    
    stats_intent = classify_statistical_intent(cleaned_utterance)
    stats_score = 0
    if stats_intent != -1:
        stats_score = 1
    
    total_score = (
        0.4 * pattern_score + 
        0.2 * sentiment_score + 
        0.2 * speech_act_score + 
        0.2 * stats_score
    )

    if total_score > 0.5:
        return match, total_score
    else:
        return -1, 0



