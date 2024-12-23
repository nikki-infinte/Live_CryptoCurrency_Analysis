import time
from crypto_fetcher import CryptoDataFetcher
from excel_updater import ExcelUpdater

def main(update_interval=300):
    """
    Main function to run the cryptocurrency data tracking system
    Args:
        update_interval (int): Time between updates in seconds (default: 300 seconds / 5 minutes)
    """
    print(f"Crypto Tracker starting. Data will update every {update_interval} seconds...")
    
    # Initialize our components
    fetcher = CryptoDataFetcher()
    excel_updater = ExcelUpdater()
    
    while True:
        try:
            # Fetch the latest data
            crypto_data = fetcher.fetch_data()
            
            # Update the Excel file
            if crypto_data is not None:
                excel_updater.update(crypto_data)
            
            # Wait for next update
            time.sleep(update_interval)
            
        except KeyboardInterrupt:
            print("\nCrypto Tracker stopped by user")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Retrying in 60 seconds...")
            time.sleep(60)

if __name__ == "__main__":
    main()