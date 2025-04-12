"""
pattern_matching.py

Brendan Dileo, April 2025
"""

from utils.process_text import clean_utterance
import regex as re

def regex_match(utterance, regex_patterns):
    for i, pattern in enumerate(regex_patterns):
        if re.match(pattern, utterance):
            print(f"Regex match found: '{utterance}' matches pattern '{pattern}' (index {i})")      # DEBUG
            return i 
    return -1