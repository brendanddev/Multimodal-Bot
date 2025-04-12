"""
pattern_matching.py

Brendan Dileo, April 2025
"""

from utils.process_text import clean_utterance
import regex as re
from fuzzywuzzy import fuzz
import Levenshtein as levenshtein


def regex_match(utterance, regex_patterns):
    """ Performs a basic string pattern match to find matching response to utterance """
    print(f"\n[DEBUG] Raw utterance: '{utterance}'")            
    cleaned = clean_utterance(utterance)
    print(f"[DEBUG] Cleaned utterance: '{cleaned}'")            

    # Go through each regex pattern, check for a match
    for i, pattern in enumerate(regex_patterns):
        match = re.match(pattern, cleaned)
        print(f"[DEBUG] Trying pattern {i}: '{pattern}'")      

        if match:
            print(f"[MATCH FOUND] Utterance: '{cleaned}' matches pattern {i}: '{pattern}'")                
            
            if match.fuzzy_counts:
                insertions, deletions, subs = match.fuzzy_counts
                print(f"[FUZZY MATCH DETAILS] Insertions: {insertions}, Deletions: {deletions}, Substitutions: {subs}")         
           
            print("Match:", match.group())
            print("Fuzzy Counts (i, d, s):", match.fuzzy_counts)
            print("Fuzzy Changes:", match.fuzzy_changes)

            return i 
        else:
            print(f"[NO MATCH] Pattern {i} did not match.")
    return -1

def fuzzy_match(utterance, intents):
    """ Fuzzy pattern matching to calculate the similarity between the users utterance and possible responses """
    best_match = None
    best_score = -1

    # Find best fuzzy match
    for intent in intents:
        score = fuzz.ratio(utterance, intent)
        print(f"Fuzzy matching '{utterance}' with intent '{intent}' gives score {score}")                              

        # Find best score
        if score > best_score:
            best_score = score
            best_match = intent 
    
    if best_match:
        print(f"[FUZZY MATCH FOUND] Best match: '{best_match}' with score {best_score}")       
    else:
        print("[NO FUZZY MATCH] No match found.")                                             

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
            print(f"[DEBUG] New best match found: '{best_match}' with distance {best_score}")

        if best_match:
            print(f"Best Levenshtein match: '{best_match}' with distance {best_score}")
        else:
            print("No Levenshtein match found.")
    return best_match, best_score


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
