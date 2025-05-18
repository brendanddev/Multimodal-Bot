# Multimodal Bot
This chatbot began as a simple FAQ bot built from the ground up using Python and basic pattern matching techniques. Through continous development, the bot has evolved into a sophisticated multimodal system that combines various approaches to natural language processing and interaction.

## Features
- Rule-based pattern matching
- Regular Expression pattern matching
- Fuzzy regular expression and string matching
- Use of Levenshtein and Heuristic pattern matching
- Named Entity Recognition
- Speech Act Classification
- Sentiment Analysis
- TF-IDF Similarity Processing
- Dialog Management
- Fallback Response System
- OpenAI Integration for fallback enhancement and custom prompt engineering
- Image Proccesing using OpenAI
- Web Scraping
- Data Visualization
- Platform Integration
- Custom XP System

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
- **SpaCy**: For NLP and entity recognition capabilities
- **Regex**: For advanced pattern matching
- **FuzzyWuzzy**: For fuzzy string matching
- **Scikit-learn**: For TF-IDF and machine learning
- **NumPy**: For numerical computing and graphs
- **BeautifulSoup**: For web scraping capabilities
- **Discord API**: For bot integration
- **SQLite**: For data persistence
- **Node.js**: For XP system backend
