
import regex as re
from fuzzywuzzy import fuzz
import Levenshtein as lev

def clean_utterance(utterance):
    clean = re.sub(r'[^\w\s]', '', utterance) 
    clean = re.sub(r'\s+', ' ', clean).strip()  
    print(f"Cleaned Utterance: '{clean}'")  
    return clean.lower()

def fuzzy_match(utterance, intents):
    best_match = None 
    best_score = -1

    for intent in intents:
        score = fuzz.ratio(utterance, intent)
        if score > best_score:
            best_score = score
            best_match = intent 

    return best_match, best_score

def fuzzy_regex_match(utterance, regex_patterns):
    best_match = None 
    best_score = -1

    for pattern in regex_patterns:
        score = fuzz.partial_ratio(utterance, pattern)
        if score > best_score:
            best_score = score
            best_match = pattern 
    return best_match, best_score


def levenshtein_match(utterance, intents):
    best_match = None 
    best_score = float('inf')

    for intent in intents:
        score = lev.distance(utterance, intent)
        if score < best_score:
            best_score = score
            best_match = intent
    return best_match, best_score

def heuristic_match(utterance, intents, regex_patterns):
    match, score = fuzzy_regex_match(utterance, regex_patterns)
    if match and score > 60:
        return regex_patterns.index(match), score
    
    match, score = fuzzy_match(utterance, intents)
    if match and score > 60:
        return intents.index(match), score
    
    match, socre = levenshtein_match(utterance, intents)
    if match:
        return intents.index(match), score 
    
    return -1, 0

def understand(utterance, intents, regex_patterns):
    cleaned_utterance = clean_utterance(utterance)

    match, score = heuristic_match(cleaned_utterance, intents, regex_patterns)
    if match != -1:
        return match
    return -1