"""
pattern_matching.py

Brendan Dileo, April 2025
"""

from utils.process_text import clean_utterance
import regex as re

def regex_match(utterance, regex_patterns):
    """ Performs a basic string pattern match to find matching response to utterance """
    print(f"\n[DEBUG] Raw utterance: '{utterance}'")            # DEBUG
    cleaned = clean_utterance(utterance)
    print(f"[DEBUG] Cleaned utterance: '{cleaned}'")            # DEBUG

    for i, pattern in enumerate(regex_patterns):
        match = re.match(pattern, cleaned)
        print(f"[DEBUG] Trying pattern {i}: '{pattern}'")       # DEBUG

        if match:
            print(f"[MATCH FOUND] Utterance: '{cleaned}' matches pattern {i}: '{pattern}'")                 # DEBUG
            
            if match.fuzzy_counts:
                insertions, deletions, subs = match.fuzzy_counts
                print(f"[FUZZY MATCH DETAILS] Insertions: {insertions}, Deletions: {deletions}, Substitutions: {subs}")         # DEBUG
           
            print("Match:", match.group())
            print("Fuzzy Counts (i, d, s):", match.fuzzy_counts)
            print("Fuzzy Changes:", match.fuzzy_changes)

            return i 
        else:
            print(f"[NO MATCH] Pattern {i} did not match.")
    return -1

def fuzzy_match(utterance, intents):
    """ Fuzzy pattern matching to calculate the similarity between the users utterance and possible responses """
    return -1