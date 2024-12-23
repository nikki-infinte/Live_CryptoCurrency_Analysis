import requests
import pandas as pd
from datetime import datetime
import openpyxl
from openpyxl.styles import PatternFill, Font
import os
import time
from pathlib import Path
import json

class CryptoAnalyzer:
    def __init__(self, excel_file='crypto_live_data.xlsx', report_file='analysis_report.md'):
        self.api_url = "https://api.coingecko.com/api/v3"
        self.excel_file = excel_file
        self.report_file = report_file
        self.historical_data = []
        
    def fetch_crypto_data(self):
        """Fetch top 50 cryptocurrencies data"""
        try:
            params = {
                'vs_currency': 'usd',
                'order': 'market_cap_desc',
                'per_page': 50,
                'page': 1,
                'sparkline': False
            }
            response = requests.get(f"{self.api_url}/coins/markets", params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def analyze_data(self, data):
        """Perform analysis on cryptocurrency data"""
        df = pd.DataFrame(data)
        
        # Basic statistics
        analysis = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'top_5_by_market_cap': df.nlargest(5, 'market_cap')[['name', 'market_cap']].to_dict('records'),
            'average_price': df['current_price'].mean(),
            'highest_24h_change': df.nlargest(1, 'price_change_percentage_24h')[['name', 'price_change_percentage_24h']].to_dict('records')[0],
            'lowest_24h_change': df.nsmallest(1, 'price_change_percentage_24h')[['name', 'price_change_percentage_24h']].to_dict('records')[0],
            'total_market_cap': df['market_cap'].sum(),
            'average_24h_volume': df['total_volume'].mean()
        }
        
        self.historical_data.append(analysis)
        return analysis

    def update_excel(self, data):
        """Update Excel with live cryptocurrency data"""
        df = pd.DataFrame(data)
        
        # Select and rename columns
        columns = {
            'name': 'Name',
            'symbol': 'Symbol',
            'current_price': 'Price (USD)',
            'market_cap': 'Market Cap',
            'total_volume': '24h Volume',
            'price_change_percentage_24h': '24h Change %'
        }
        
        df = df[columns.keys()].rename(columns=columns)
        df['Last Updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Save to Excel with formatting
        with pd.ExcelWriter(self.excel_file, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Live Data')
            self._format_excel(writer)
        
        return df

    def _format_excel(self, writer):
        """Apply formatting to Excel worksheet"""
        worksheet = writer.sheets['Live Data']
        
        # Format headers
        header_fill = PatternFill(start_color='1F4E78', end_color='1F4E78', fill_type='solid')
        header_font = Font(color='FFFFFF', bold=True)
        
        for cell in worksheet[1]:
            cell.fill = header_fill
            cell.font = header_font
            
        # Adjust column widths
        for column in worksheet.columns:
            max_length = max(len(str(cell.value)) for cell in column)
            worksheet.column_dimensions[column[0].column_letter].width = max_length + 2

    def generate_report(self):
        """Generate analysis report in Markdown format"""
        if not self.historical_data:
            return
        
        latest = self.historical_data[-1]
        
        report = f"""# Cryptocurrency Market Analysis Report
Generated on: {latest['timestamp']}

## Top 5 Cryptocurrencies by Market Cap
"""
        
        for i, crypto in enumerate(latest['top_5_by_market_cap'], 1):
            report += f"{i}. {crypto['name']}: ${crypto['market_cap']:,.2f}\n"
        
        report += f"""
## Market Statistics
- Average Price: ${latest['average_price']:,.2f}
- Total Market Cap: ${latest['total_market_cap']:,.2f}
- Average 24h Volume: ${latest['average_24h_volume']:,.2f}

## Price Changes (24h)
- Highest: {latest['highest_24h_change']['name']} ({latest['highest_24h_change']['price_change_percentage_24h']:.2f}%)
- Lowest: {latest['lowest_24h_change']['name']} ({latest['lowest_24h_change']['price_change_percentage_24h']:.2f}%)

## Analysis Period
- Start Time: {self.historical_data[0]['timestamp']}
- End Time: {latest['timestamp']}
- Total Updates: {len(self.historical_data)}
"""
        
        with open(self.report_file, 'w') as f:
            f.write(report)