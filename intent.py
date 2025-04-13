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

def understand(utterance, intents, regex_patterns):
    """ Processes an utterance to determine if an intent matches"""
    cleaned_utterance = clean_utterance(utterance)
    ling_info = extract_linguistics(utterance)
    ling_patterns = match_patterns(utterance)
    print(ling_info)
    print(ling_patterns)
    intent = heuristic_match(cleaned_utterance, intents, regex_patterns)
    return intent 

def generate(intent, responses):
    """ Attempts to return an appropriate response given a users intent """
    if intent == -1:
        return "Sorry, I don't know the answer to that!"
    return responses[intent]

