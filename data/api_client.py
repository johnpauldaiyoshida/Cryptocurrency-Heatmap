import requests
import logging
from config.constants import COINGECKO_API_URL
from typing import List, Dict

def fetch_crypto_data():
    """Fetches data from CoinGecko API with error handling"""
    try:
        response = requests.get(f"{COINGECKO_API_URL}/coins/markets?vs_currency=usd")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None  # Fallback to cached data