""" 
intent.py

This script implements the logic to allow the bot to anwser a predefined
question from a list of predefined responses using basic string matching.

Brendan Dileo, April 2025
"""

def understand(utterance, intents):
    """ Processes an utterance to determine if an intent matches"""
    try:
        return intents.index(utterance)
    except ValueError: 
        return -1

def generate(intent, responses):
    """ Attempts to return an appropriate response given a users intent """
    if intent == -1:
        return "Sorry, I don't know the answer to that!"
    return responses[intent]

