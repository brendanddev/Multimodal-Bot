# Multimodal Bot
A sophisticated multimodal chatbot system that combines natural language processing, image processing, web scraping, and advanced analytics capabilities. This project implements a versatile bot that can process both text and image inputs, providing intelligent responses through various platforms while maintaining user engagement through an XP system and advanced analytics.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/multimodal-bot.git
   cd multimodal-bot
   ```
2. Set up Python environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e .
   ```
3. Set up Node.js environment:
   ```bash
   cd server_api
   npm install
   ```
4. Set up environment variables:
   Create a `.env` file in the project root with:
   ```
   OPENAI_API_KEY=your_api_key_here
   DISCORD_TOKEN=your_discord_token_here
   DATABASE_URL=sqlite:///server_api/xp_system.db
   ```

## Usage
1. Start the XP System Server:
   ```bash
   cd server_api
   node server.js
   ```

2. Start the Bot:
   ```bash
   python main.py
   ```

## Acknowledgements
