
"""
dialog_management.py

Brendan Dileo, April 2025
"""

import json 
CONVERSATION_FILE = "data/conversation_history.json"

def read_conversation_history():
    try:
        with open(CONVERSATION_FILE, "r") as file:
            history = json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        history = []
        print("No previous conversation history found or file is empty")
    return history

def save_conversation_history(history):
    try:
        with open(CONVERSATION_FILE, "w") as file:
            json.dump(history, file, indent=4)
    except Exception as e:
        print(f"Error saving conversation history: {e}")