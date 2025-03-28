
from fuzzywuzzy import fuzz
import Levenshtein as lev

def fuzzy_match(utterance, intents):
    """
    Fuzzy match the input utterance with the given intents using fuzzywuzzy.
    """
    best_match = None 
    best_score = -1

    for intent in intents:
        score = fuzz.ratio(utterance, intent)
        if score > best_score:
            best_score = score
            best_match = intent 

    return best_match, best_score


def fuzzy_regex_match(utterance, regex_patterns):
    """
    Fuzzy regex match the input utterance with the given regex patterns.
    """
    best_match = None 
    best_score = -1

    for pattern in regex_patterns:
        score = fuzz.partial_ratio(utterance, pattern)
        if score > best_score:
            best_score = score
            best_match = pattern 
    return best_match, best_score


def levenshtein_match(utterance, intents):
    """
    Levenshtein match the input utterance with the given intents.
    """
    best_match = None 
    best_score = float('inf')

    for intent in intents:
        distance = lev.distance(utterance, intent)

        max_length = max(len(utterance), len(intent))
        similarity = 1 - (distance / max_length) 

        if distance < best_score and similarity > 0.7:  # ~70% similarity
            best_score = distance
            best_match = intent

    return best_match, best_score


def heuristic_match(utterance, intents, regex_patterns):
    """
    Try multiple matching techniques and return the best match.
    """
    match, score = fuzzy_regex_match(utterance, regex_patterns)
    if match and score > 60:
        print("Fuzzy Regex Match")
        return regex_patterns.index(match), score
    
    match, score = fuzzy_match(utterance, intents)
    if match and score > 60:
        print("Fuzzy Match")
        return intents.index(match), score
    
    match, score = levenshtein_match(utterance, intents)
    if match:
        print("Levenshtein Match")
        return intents.index(match), score 
    
    return -1, 0
