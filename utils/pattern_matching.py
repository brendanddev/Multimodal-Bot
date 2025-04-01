
"""
A hybrid pattern matching approach that combines rule-based pattern matching
with fuzzy matching and Levenshtein distance to determine the best match for
a users utterance.
"""

from utils.process_text import clean_utterance
import regex as re
from fuzzywuzzy import fuzz
import Levenshtein as levenshtein

def regex_match(utterance, regex_patterns):
    for i, pattern in enumerate(regex_patterns):
        if re.match(pattern, utterance):
            print(f"Regex match found: '{utterance}' matches pattern '{pattern}' (index {i})")
            return i 
    print(f"No regex match found for: '{utterance}'")
    return -1

def fuzzy_match(utterance, intents):
    best_match = None 
    best_score = -1

    for intent in intents:
        score = fuzz.ratio(utterance, intent)
        print(f"Fuzzy matching '{utterance}' with intent '{intent}' gives score {score}")
        if score > best_score:
            best_score = score
            best_match = intent
        if best_match:
            print(f"Fuzzy matching '{utterance}' with intent '{intent}' gives score {score}")
        else:
            print("No fuzzy match found.")
    return best_match, best_score

def levenshtein_match(utterance, intents):
    best_match = None
    best_score = float('inf') 

    for intent in intents:
        distance = levenshtein.distance(utterance, intent)
        print(f"Levenshtein distance between '{utterance}' and '{intent}' is {distance}")
        if distance < best_score:
            best_score = distance
            best_match = intent
        if best_match:
            print(f"Best Levenshtein match: '{best_match}' with distance {best_score}")
        else:
            print("No Levenshtein match found.")
    return best_match, best_score

def heuristic_match(utterance, intents, regex_patterns):
    cleaned_utterance = clean_utterance(utterance)

    # Try basic regex pattern matching
    re_match = regex_match(cleaned_utterance, regex_patterns)
    if re_match != -1:
        return re_match
    
    # Try fuzzy match (similarity based)
    fuzz_match, fuzz_score = fuzzy_match(cleaned_utterance, intents)
    if fuzz_match and fuzz_score > 60: # adjust this?
        return intents.index(fuzz_match)
    
    lev_match, lev_score = levenshtein_match(cleaned_utterance, intents)
    if lev_match and lev_score < 5:
        return intents.index(lev_match)
    return -1
