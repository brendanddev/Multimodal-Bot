"""
process_text.py

This script cleans and normalizes the user utterance.

Brendan Dileo, April 2025
"""

import regex as re

def clean_utterance(utterance):
    """ Cleans the users utterance from non word cgaracrers and spacing """
    clean = re.sub(r'[^\w\s]', '', utterance)               # non letter words
    clean = re.sub(r'\s+', ' ', clean).strip()              # multiple spaces
    return clean.lower()


