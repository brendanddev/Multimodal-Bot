"""
pattern_matching.py

Brendan Dileo, April 2025
"""

from process_text import clean_utterance
import regex as re
from fuzzywuzzy import fuzz


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
    """ Fuzzy pattern matching to calculate the similarity between the user's utterance and possible responses """
    best_match = None
    best_score = -1

    # Find best fuzzy match
    for intent in intents:
        ratio_score = fuzz.ratio(utterance, intent)
        partial_score = fuzz.partial_ratio(utterance, intent)
        token_sort_score = fuzz.token_sort_ratio(utterance, intent)
        token_set_score = fuzz.token_set_ratio(utterance, intent)
        partial_token_sort_score = fuzz.partial_token_sort_ratio(utterance, intent)

        print(f"Fuzzy matching '{utterance}' with intent '{intent}' gives scores:")
        print(f"  - ratio: {ratio_score}")
        print(f"  - partial_ratio: {partial_score}")
        print(f"  - token_sort_ratio: {token_sort_score}")
        print(f"  - token_set_ratio: {token_set_score}")
        print(f"  - partial_token_sort_ratio: {partial_token_sort_score}")

        # Compare all scores and keep track of the best one
        best_local_score = max(ratio_score, partial_score, token_sort_score, token_set_score, partial_token_sort_score)

        # Find best score
        if best_local_score > best_score:
            best_score = best_local_score
            best_match = intent

    if best_match:
        print(f"[FUZZY MATCH FOUND] Best match: '{best_match}' with score {best_score}")
    else:
        print("[NO FUZZY MATCH] No match found.")

    return best_match, best_score


# Local file tests
if __name__ == "__main__":
    utterance = "what is linguistic knowledg"
    regex_patterns = [
        r"^what\s+(is|does)\s+(nlp|natural\s+language\s+processing)\s*(do)?$",
        r"^what\s+(is|does)\s+(chat\s+bot|faq\s+bot)\s*(do)?$",
        r"^what\s+(is|does)\s+(linguistic\s+knowledge)\s*(do)?$"
    ]
    intents = [
        "What is natural language processing?",
        "What does a chatbot do?",
        "What is linguistic knowledge?"
    ]

    print("[DEBUG] Running regex match...\n")
    regex_index = regex_match(utterance, regex_patterns)
    print(f"Regex match index: {regex_index}\n")

    print("[DEBUG] Running fuzzy match...\n")
    best_match, best_score = fuzzy_match(utterance, intents)
    print(f"Best fuzzy match: '{best_match}' with score {best_score}")
