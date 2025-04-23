
"""
scraper.py


Brendan Dileo, April 2025

Some scraping logic adapted from: 
@wyanthd - https://www.tiktok.com/@wyanthd
"""

import requests
from bs4 import BeautifulSoup       # Web scraping lib

def scrape(url):
    # GET request to url
    response = requests.get(url)

    # Check if response is successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Retreive all h2 and p tags
        headlines = soup.select('h2')
        paragraphs = soup.find_all('p')

        if not headlines:
            print("No headlines found with the selector 'h2'")
        
        if not paragraphs:
            print("No paragraphs found with the selector 'p'")
        
        # Cleans the scraped headline data
        cleaned_headlines = []
        for headline in headlines:
            text = headline.get_text(strip=True)
            if text:
                cleaned_headlines.append(text)
        
        # Cleans the scraped paragraph data
        cleaned_paragraphs = []
        for paragraph in paragraphs:
            text = paragraph.get_text(strip=True)
            if text:
                cleaned_paragraphs.append(text)
        
        print("Headlines:")
        for idx, headline in enumerate(cleaned_headlines, 1):
            print(f"{idx}. {headline}")
        
        print("\nParagraphs:")
        for idx, paragraph in enumerate(cleaned_paragraphs, 1):
            print(f"{idx}. {paragraph}")
        
        return cleaned_headlines, cleaned_paragraphs
    else:
        print('An error occurred while making the request!')
        return []

# Gamespot URL
url = "https://www.cbc.ca/news"
scrape(url)
