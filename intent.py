""" 
intent.py

This script implements the logic to allow the bot to anwser a predefined
question from a list of predefined responses using basic string matching.

Brendan Dileo, April 2025
"""

from utils.process_text import clean_utterance
from utils.pattern_matching import heuristic_match
from utils.linguistic_extraction import extract_linguistics
from utils.linguistic_patterns import match_patterns
from openai_init import get_openai_response

def understand(utterance, intents, regex_patterns):
    """ Processes an utterance to determine if an intent matches"""
    cleaned_utterance = clean_utterance(utterance)
    intent = heuristic_match(cleaned_utterance, intents, regex_patterns)
    return intent 

def generate(intent, responses, utterance=None):
    """ Attempts to return an appropriate response given a users intent """
    if intent == -1:
        print("OpenAI Call")
        return get_openai_response(utterance or "")
    return responses[intent]

