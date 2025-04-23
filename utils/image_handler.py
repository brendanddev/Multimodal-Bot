
"""
image_handler.py

Handles the Discord related user interactions.

Brendan Dileo, April 2025
"""

import os 
import asyncio
import discord 
from openai_images import analyze_image

async def handle_image_analysis(message: discord.Message):