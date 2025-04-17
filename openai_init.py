"""
openai.py

Brendan Dileo, April 2025
"""

from openai import OpenAI
from config import OPENAI_API_KEY

# Initialize the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def get_openai_response(utterance):
    messages = [
        {"role": "system", "content": "You are a helpful bot that only answers general knowledge or questions not covered by predefined intents."},
        {"role": "user", "content": utterance}
    ]
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.0,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error occurred while fetching response: {e}")
        return "Sorry, something went wrong while processing your request."