# Chapter 12: Advanced Topics (Web Scraping)

import requests
from bs4 import BeautifulSoup

# Web Scraping with BeautifulSoup

# Function to scrape quotes from http://quotes.toscrape.com
def scrape_quotes():
    url = "http://quotes.toscrape.com"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting quotes
        quotes = soup.find_all('span', class_='text')
        for index, quote in enumerate(quotes, start=1):
            print(f"Quote {index}: {quote.text.strip()}\n")

    else:
        print(f"Failed to fetch the webpage. Status Code: {response.status_code}")

# Calling the function to scrape quotes
scrape_quotes()

# Explanation:
# - The `requests` library is used to fetch the HTML content of a webpage.
# - BeautifulSoup is used to parse and navigate the HTML.
# - In this example, quotes are scraped from http://quotes.toscrape.com by targeting the specific HTML elements.

