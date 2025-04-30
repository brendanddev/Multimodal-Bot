""" 
load_data.py

This script reads json data.

Brendan Dileo, April 2025
"""

import json 

def load_json_data():
    try:
        with open("data/data.json", "r") as file:
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

def load_regex_patterns():
    try:
        with open("data/fuzzy_regex.txt", "r") as file:
            patterns = file.readlines()
        return [pattern.strip() for pattern in patterns]
    except FileNotFoundError:
            print(f"Error: The file was not found!")
    except Exception as e:
            print(f"An unexpected error occurred while loading the patterns: {e}")
    return []

def load_response_data():
    try:
        with open("data/interactions.json", "r") as file:
            intents = json.load(file)
            return intents 
    except FileNotFoundError:
            print(f"Error: The file was not found!")
    except Exception as e:
            print(f"An unexpected error occurred while loading the patterns: {e}")
    return []