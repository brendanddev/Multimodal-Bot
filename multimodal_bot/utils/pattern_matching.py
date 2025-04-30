"""
pattern_matching.py

Brendan Dileo, April 2025
"""

import regex as re
from fuzzywuzzy import fuzz
import Levenshtein as levenshtein

def clean_utterance(utterance):
    """ Cleans the users utterance from non word cgaracrers and spacing """
    clean = re.sub(r'[^\w\s]', '', utterance)               
    clean = re.sub(r'\s+', ' ', clean).strip()             
    return clean.lower()

def regex_match(utterance, regex_patterns):
    """ Performs a basic string pattern match to find matching response to utterance """
    cleaned = clean_utterance(utterance)

    # Go through each regex pattern, check for a match
    for i, pattern in enumerate(regex_patterns):
        match = re.match(pattern, cleaned)
        if match:            
            return i 
    return -1

def fuzzy_match(utterance, intents):
    """ Fuzzy pattern matching to calculate the similarity between the users utterance and possible responses """
    best_match = None
    best_score = -1

    # Find best fuzzy match
    for intent in intents:
        score = fuzz.ratio(utterance, intent)

        # Find best score
        if score > best_score:
            best_score = score
            best_match = intent                                         
    return best_match, best_score

def levenshtein_match(utterance, intents):
    """ Levenshtein distance to find the difference between two strings """
    best_match = None 
    best_score = float('inf')

    # Go through intents
    for intent in intents:
        distance = levenshtein.distance(utterance, intent)
        
        # Find smallest distance
        if distance < best_score:
            best_score = distance
            best_match = intent
        
        # Threshold for distance to reduce false positive matches
        if best_score < 3.5:
            return best_match, best_score
        else:
            return None, best_score


def heuristic_match(utterance, intents, regex_patterns):
    """ Combines each approach to determine the best possible match """
    cleaned = clean_utterance(utterance)

    # Try regex matching
    re_match = regex_match(cleaned, regex_patterns)
    if re_match != -1:
        return re_match
    
    # Try fuzzy if regex dosent work
    fuzz_match, fuzz_score = fuzzy_match(cleaned, intents)
    if fuzz_match and fuzz_score > 60:      # Check this 
        return intents.index(fuzz_match)
    
    lev_match, lev_score = levenshtein_match(cleaned, intents)
    if lev_match:
        return intents.index(lev_match)
    
    return -1
