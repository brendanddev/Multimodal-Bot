""" 
intent.py

This script implements the logic to allow the bot to anwser a predefined
question from a list of predefined responses using basic string matching.

Brendan Dileo, April 2025
"""

from utils.process_text import clean_utterance
from utils.pattern_matching import heuristic_match
from openai_init import get_openai_response
from utils.interactions import detect_response

def understand(utterance, intents, regex_patterns):
    """ Processes an utterance to determine if an intent matches"""
    cleaned_utterance = clean_utterance(utterance)

    detected_response = detect_response(cleaned_utterance)
    if detected_response:
        return detected_response, None

    intent = heuristic_match(cleaned_utterance, intents, regex_patterns)
    return None, intent 

def generate(intent, response, responses, utterance=None):
    """ Attempts to return an appropriate response given a users intent """
    if response:
        return response
    
    if intent is not None and intent != -1:
            return responses[intent]

    print("OpenAI Call")
    return get_openai_response(utterance or "")
