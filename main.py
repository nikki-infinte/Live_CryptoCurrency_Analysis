import time
from datetime import datetime
import os
from crypto_analyzer import CryptoAnalyzer

def main():
    """
    Main function to run the cryptocurrency tracking system.
    Fetches data every 5 minutes, updates Excel, and generates analysis.
    """
    # Initialize the analyzer
    analyzer = CryptoAnalyzer(
        excel_file='crypto_data.xlsx',
        report_file='analysis_report.md'
    )
    
    # Set update interval (5 minutes)
    update_interval = 300
    
    print("\n=== Cryptocurrency Tracker Starting ===")
    print(f"Update Interval: {update_interval} seconds")
    print(f"Excel File: {os.path.abspath(analyzer.excel_file)}")
    print(f"Report File: {os.path.abspath(analyzer.report_file)}")
    print("=====================================\n")
    
    while True:
        try:
            # Get current timestamp
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"\nStarting update at {current_time}")
            
            # 1. Fetch cryptocurrency data
            print("Fetching cryptocurrency data...")
            crypto_data = analyzer.fetch_crypto_data()
            
            if crypto_data is not None:
                # 2. Analyze the data
                print("Analyzing data...")
                analysis = analyzer.analyze_data(crypto_data)
                
                # 3. Update Excel file
                print("Updating Excel file...")
                analyzer.update_excel(crypto_data)
                
                # 4. Generate analysis report
                print("Generating report...")
                analyzer.generate_report()
                
                print(f"Update completed successfully")
            else:
                print("Failed to fetch data")
            
            # Wait for next update
            print(f"Waiting {update_interval} seconds until next update...")
            time.sleep(update_interval)
            
        except KeyboardInterrupt:
            print("\nProgram stopped by user")
            print("Generating final report...")
            analyzer.generate_report()
            break
            
        except Exception as e:
            print(f"\nError occurred: {str(e)}")
            print("Retrying in 60 seconds...")
            time.sleep(60)

if __name__ == "__main__":
    main()