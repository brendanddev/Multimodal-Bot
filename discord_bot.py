"""
discord.py

Brendan Dileo, April 2025
"""

import discord
from bot import generate, understand, intents, responses, regex_patterns
from config import DISCORD_TOKEN
from utils.process_text import clean_utterance
from datetime import datetime


# MyClient class def
class MyClient(discord.Client):

    def __init__(self):
        bot_intents = discord.Intents.default()
        bot_intents.message_content = True
        super().__init__(intents=bot_intents)

    async def on_ready(self):
        print('Logged on as', self.user)
        self.start_time = datetime.now()

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('!'):
            cmd = clean_utterance(message.content)

            if cmd == "ping":
                await message.channel.send("Pong!")
            else:
                await message.channel.send("Sorry, I don't recognize that command!")

        utterance = message.content

        intent = understand(utterance, intents, regex_patterns)
        response = generate(intent, responses)

        await message.channel.send(response)

client = MyClient()
client.run(DISCORD_TOKEN)
