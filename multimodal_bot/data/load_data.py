""" 
load_data.py

This script reads json data.

Brendan Dileo, April 2025
"""

import json 
import os

def get_data_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

# Load basic json data for predefined questions and answers
def load_json_data():
    try:
        with open(get_data_path("data.json"), "r") as file:
            data = json.load(file) 
            print("Data Loaded Successfully!") 
        return data["questions"], data["answers"]
    except FileNotFoundError:
        print("Error: The data file is missing!")
    except json.JSONDecodeError: 
        print("Error: There was an issue decoding the JSON data!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return [], []

# Loads the fuzzy regex patterns
def load_regex_patterns():
    try:
        with open(get_data_path("fuzzy_regex.txt"), "r") as file:
            patterns = file.readlines()
        return [pattern.strip() for pattern in patterns]
    except FileNotFoundError:
            print(f"Error: The file was not found!")
    except Exception as e:
            print(f"An unexpected error occurred while loading the patterns: {e}")
    return []

# Loads the fallback response data
def load_fallback_data():
    try:
        with open(get_data_path("fallback.json"), "r") as file:
            data = json.load(file)
            return data["fallbacks"], data["question_fallbacks"], data["command_fallbacks"], data["statement_fallbacks"]
    except FileNotFoundError: 
        print("Error: The data file is missing!")
    except json.JSONDecodeError: 
        print("Error: There was an issue decoding the JSON data!")
    except Exception as e: 
        print(f"An unexpected error occurred: {e}")
        return [], [], [], []

# Load the predefined enitity responses
def load_entitiy_responses():
    try:
        with open("data/fallback.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError: 
        print("Error: The data file is missing!")
    except json.JSONDecodeError: 
        print("Error: There was an issue decoding the JSON data!")
    except Exception as e: 
        print(f"An unexpected error occurred: {e}")
        return {}