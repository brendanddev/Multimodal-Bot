""" 
intent.py

This script implements the logic to allow the bot to anwser a predefined
question from a list of predefined responses using basic string matching.

Brendan Dileo, April 2025
"""

from multimodal_bot.utils.pattern_matching import clean_utterance
from multimodal_bot.utils.pattern_matching import heuristic_match
from multimodal_bot.api.openai_init import get_openai_response
from multimodal_bot.utils.fallback import fallback_response

def understand(utterance, intents, regex_patterns):
    """ Processes an utterance to determine if an intent matches"""
    cleaned_utterance = clean_utterance(utterance)
    intent = heuristic_match(cleaned_utterance, intents, regex_patterns)
    return None, intent 

def generate(intent, response, responses, utterance=None):
    """ Attempts to return an appropriate response given a users intent """
    if response:
        return response
    
    if intent is not None and intent != -1:
            return responses[intent]

    print("Fallback")
    return fallback_response(utterance)
