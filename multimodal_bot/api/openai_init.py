"""
openai.py

Brendan Dileo, April 2025
"""

from openai import OpenAI
from multimodal_bot.config.config import OPENAI_API_KEY
from multimodal_bot.utils.dialog_management import read_conversation_history, save_conversation_history
from multimodal_bot.utils.sentiment import analyze_sentiment

# Initialize the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def construct_response(utterance, sentiment, emotion):
    if emotion == "happy":
        tone = "cheerful and positive"
    elif emotion == "sad":
        tone = "empathetic and supportive"
    elif emotion == "neutral":
        tone = "neutral and informative"
    else:
        tone = "general"
        
    if sentiment == "positive":
        response = f"Respond with a {tone} but optimistic response to the positive sentiment in this utterance: '{utterance}'"
    elif sentiment == "negative":
        response = f"Respond with a {tone} and encouraging response to the negative sentiment in this utterance: '{utterance}'"
    elif sentiment == "neutral":
        response = f"Provide a {tone} and balanced response to this neutral statement: '{utterance}'"
    else:
        response = f"Provide a {tone} and understanding response to this utterance: '{utterance}'"
    
    return response

def get_openai_response(utterance):
    # Analyze sentiment & emotion
    sentiment, emotion = analyze_sentiment(utterance)
    prompt = construct_response(utterance, sentiment, emotion)
    
    # Load convo history
    conversation_history = read_conversation_history()
    conversation_history.append({"role": "user", "content": utterance})
    
    # Set limit to storage amount
    limit = 6
    if len(conversation_history) > limit:
        conversation_history = conversation_history[-limit:]  
    
    messages = [{"role": "system", "content": "You are a helpful bot that only answers general knowledge or questions not covered by predefined intents."}]
    for entry in conversation_history:
        messages.append(entry)

    # Add constructed response
    messages.append({"role": "user", "content": prompt})        

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