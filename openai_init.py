"""
openai.py

Brendan Dileo, April 2025
"""

from openai import OpenAI
from config import OPENAI_API_KEY
from utils.dialog_management import read_conversation_history, save_conversation_history

# Initialize the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def determine_intent(utterance):
    return None

def get_openai_response(utterance):

    conversation_history = read_conversation_history()
    conversation_history.append({"role": "user", "content": utterance})
    
    limit = 6
    if len(conversation_history) > limit:
        conversation_history = conversation_history[-limit:]  
    
    messages = [{"role": "system", "content": "You are a helpful bot that only answers general knowledge or questions not covered by predefined intents."}]
    for entry in conversation_history:
        messages.append(entry)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.0,
            max_tokens=150
        )

        response = response.choices[0].message.content.strip()
        save_conversation_history(conversation_history)
        return response
    except Exception as e:
        print(f"Error occurred while fetching response: {e}")
        return "Sorry, something went wrong while processing your request."