"""
openai_images.py

Brendan Dileo, April 2025

Portions of this code were adapted from OpenAI's official documentation:
https://platform.openai.com/docs/guides/images-vision
"""

import base64
from openai import OpenAI
from config import OPENAI_API_KEY

# Initialize the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Encode the image
def encode_image(path):
    with open(path, 'rb') as file:
        return base64.b64encode(file.read()).decode('utf-8')

def analyze_image(path: str, prompt: str = "What is in this image?") -> str:
    base64_image = encode_image(path)
    
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "user",
                "content": [
                    { "type": "text", "text": "What is in this image?" },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
    )
    return response.choices[0].message.content