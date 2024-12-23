![Cryptocurrency Analysis](https://worldoverviewers.com/wp-content/uploads/2023/05/648c2fcb49582300010a17a7_Fundamental-Analysis-in-Crypto-Trading-1600-900.png)


# Live Cryptocurrency Data Analysis

## Fetching and Analyzing Top 50 Live Cryptocurrency Data

### Objective
The goal of this project is to fetch live cryptocurrency data for the top 50 cryptocurrencies, analyze it, and present the data in a live-updating Excel sheet. The Excel sheet will continuously update with the latest cryptocurrency prices.

---

## Features
1. **Fetch Live Data**:
   - Utilizes a public API (e.g., CoinGecko, CoinMarketCap, or Binance API) to fetch data for the top 50 cryptocurrencies by market capitalization.
   - Includes the following fields:
     - Cryptocurrency Name
     - Symbol
     - Current Price (in USD)
     - Market Capitalization
     - 24-hour Trading Volume
     - Price Change (24-hour, percentage)

2. **Data Analysis**:
   - Identifies the top 5 cryptocurrencies by market capitalization.
   - Calculates the average price of the top 50 cryptocurrencies.
   - Analyzes the highest and lowest 24-hour percentage price change among the top 50 cryptocurrencies.

3. **Live-Running Excel Sheet**:
   - Automatically updates every 5 minutes with live cryptocurrency data.
   - Displays all fetched fields and key metrics in a structured Excel sheet.

4. **Reports**:
   - Generates an analysis report summarizing key insights and analysis.

---

## Project Structure
```
Crypto_Analysis/
├── crypto_analyzer.py        # Core module for fetching, analyzing, and updating data
├── main.py                   # Entry point for the program
├── crypto_data.xlsx          # Excel sheet for live cryptocurrency data
├── analysis_report.md        # Generated analysis report
└── README.md                 # Project documentation
```

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/nikki-infinte/Live_Crypto_Analysis.git
   cd Live_Crypto_Analysis
   ```

2. **Set Up the Environment**:
   - Ensure Python 3.x is installed.
   - Install required libraries:
     ```bash
     pip install requests openpyxl pandas
     ```

3. **Set Up API Key**:
   - Obtain an API key from your chosen cryptocurrency data provider (e.g., CoinGecko).
   - Replace the placeholder in `crypto_analyzer.py` with your API key.

---

## Usage

1. Run the program:
   ```bash
   python main.py
   ```

2. The program will:
   - Fetch live data from the API.
   - Update the Excel sheet (`crypto_data.xlsx`) every 5 minutes.
   - Generate a live-updated analysis report in `analysis_report.md`.

3. Stop the program using `CTRL+C` to generate the final report.

---

## Example Output

### Excel Sheet
An automatically updated Excel sheet with fields:
- **Name**: Bitcoin
- **Symbol**: BTC
- **Price (USD)**: $27,000
- **Market Cap**: $500 billion
- **24h Volume**: $30 billion
- **Price Change (24h)**: +2.5%

### Analysis Report
A brief report summarizing:
- **Top 5 Cryptocurrencies by Market Cap**: Bitcoin, Ethereum, Binance Coin, etc.
- **Average Price**: $1,200
- **Highest Price Change (24h)**: +12% (Cryptocurrency Name)
- **Lowest Price Change (24h)**: -8% (Cryptocurrency Name)

---

## Submission Requirements

1. Python script (`main.py`, `crypto_analyzer.py`).
2. Excel sheet (`crypto_data.xlsx`) showing live updating data.
3. Analysis Report (`analysis_report.md`) summarizing key insights.

---



## Contact
For any inquiries, please reach out to [Nikita Pawar](mailto:nikki@example.com).

