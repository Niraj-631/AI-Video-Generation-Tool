import os
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()  # Load .env variables

def get_trending_headlines():
    api_key = os.getenv("NEWS_API_KEY")
    newsapi = NewsApiClient(api_key=api_key)
    top = newsapi.get_top_headlines(language='en', page_size=5)
    return [f"{a['title']}: {a['description']}" for a in top['articles']]
