"""
openai_images.py

Brendan Dileo, April 2025
"""

import base64
from openai import OpenAI
from config import OPENAI_API_KEY

# Initialize the OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)