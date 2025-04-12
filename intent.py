""" 
intent.py

This script implements the logic to allow the bot to anwser a predefined
question from a list of predefined responses using basic string matching.

Brendan Dileo, April 2025
"""

from utils.process_text import clean_utterance
from utils.pattern_matching import regex_match

def understand(utterance, regex_patterns):
    """ Processes an utterance to determine if an intent matches"""
    cleaned_utterance = clean_utterance(utterance)
    print(f"Initial Utterance {utterance}")         # DEBUG
    print(f"Cleaned Utterance {cleaned_utterance}") # DEBUG

    intent = regex_match(cleaned_utterance, regex_patterns)
    return intent 

def generate(intent, responses):
    """ Attempts to return an appropriate response given a users intent """
    if intent == -1:
        return "Sorry, I don't know the answer to that!"
    return responses[intent]

