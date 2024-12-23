import requests 
import pandas as pd
from datetime import datetime


class CryptoDataFetcher:
    def __init__(self):
        self.api_url="https://api.coingecko.com/api/v3"

    def fetch_data(self):
        """ Fetch top 50 crypto-currency data from CoinGecko API"""
        try:
            endpoint = f"{self.api_url}/coins/markets"
            params = {
                'vs_currency': 'usd',
                'order': 'market_cap_desc',
                'per_page': 50,
                'page': 1,
                'sparkline': False
            }
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return self._process_data(response.json())
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
        
    def _process_data(self,raw_data):
        """Process raw cryptocurrency data into a pandas DataFrame"""
        if not raw_data:
            return None

        df = pd.DataFrame(raw_data)
        required_columns = [
            'symbol', 'name', 'current_price', 'market_cap', 'total_volume',
            'price_change_percentage_24h', 'circulating_supply'
        ]
        df = df[required_columns]
        
        # Calculate additional metrics
        df['market_cap_normalized'] = df['market_cap'] / df['market_cap'].sum() * 100
        df['volume_to_market_cap'] = df['total_volume'] / df['market_cap']
        
        # Rename columns for clarity
        df.columns = [
            'Symbol', 'Name', 'Price (USD)', 'Market Cap', 'Volume (24h)',
            '24h Change %', 'Circulating Supply', 'Market Share %', 'Volume/Market Cap Ratio'
        ]
        
        # Add timestamp
        df['Last Updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        return df

