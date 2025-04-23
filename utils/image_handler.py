
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
    if not message.attachments:
        await message.channel.send("Uh oh! No image was attached. Please attach an image then use the '!analyze' command.")
        return

    # Retreive attachment from user message
    attachment = message.attachments[0]
    # Make sure attachment is valid image type
    if not attachment.filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        await message.channel.send("Only JPG and PNG images are supported.")
        return

    try:
        # Creates a temp path to store the image and saves it
        image_path = f"/tmp/{attachment.filename}"
        await attachment.save(image_path)
        await message.channel.send("Analyzing image...")

        result = analyze_image(image_path)
        await message.channel.send(f"Image Analysis Result:\n{result}")
    except Exception as e:
        await message.channel.send(f"Something went wrong while analyzing the image: `{str(e)}`")
    finally:
        await asyncio.sleep(5)
        if os.path.exists(image_path):
            os.remove(image_path)