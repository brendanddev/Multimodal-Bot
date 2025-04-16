"""
config.py

Loads environment variables from the .env file.
Brendan Dileo, April 2025
"""

import os
from dotenv import load_dotenv

# Load variables from keys/.env
load_dotenv(dotenv_path="keys/.env")

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")