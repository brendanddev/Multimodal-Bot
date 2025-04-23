
"""
scraper.py


Brendan Dileo, April 2025

Some scraping logic adapted from: 
@wyanthd - https://www.tiktok.com/@wyanthd
"""

import requests
from bs4 import BeautifulSoup       # Web scraping lib

# Test func
def game_news_scrape_test():
    # Gamespot URL to be scraped
    url = "https://www.gamespot.com/news/"
    # GET request made to the URL
    response = requests.get(url)
    print('Request Made to URL')

    # Check if the response was succesful
    if response.status_code == 200:
        print('Request Successful!')
        # Creates the soup object containing web data
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Retreive first 5 h2 elements from html
        headlines = soup.select("h2")[:5]

        # Check for unsuccessful tagging
        if not headlines:
            print("No headlines found with selector 'h2'.")
            return []

        # Cleans up the scraped data to return only text contents of h2 tags (headlines)
        cleaned_headlines = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

        if cleaned_headlines:
            print("Top 5 Game News Headlines:")
            for i, headline in enumerate(cleaned_headlines, 1):
                print(f"{i}. {headline}")
        else:
            print("No headlines to display.")

        return cleaned_headlines
    else:
        print('An error occurred while making the request!')
        return []

game_news_scrape_test()