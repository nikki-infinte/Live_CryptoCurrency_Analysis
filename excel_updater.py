import pandas as pd
from openpyxl.styles import PatternFill, Font
import os

class ExcelUpdater:
    def __init__(self, filename='crypto_data.xlsx'):
        self.filename = filename

    def update(self, df):
        """Update Excel file with new data and formatting"""
        if df is None:
            print("No data to update")
            return False

        try:
            # Save to Excel with formatting
            with pd.ExcelWriter(self.filename, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Crypto Data')
                
                # Get the workbook and worksheet
                workbook = writer.book
                worksheet = writer.sheets['Crypto Data']

                # Format headers
                for cell in worksheet[1]:
                    cell.fill = PatternFill(start_color='1F4E78', end_color='1F4E78', fill_type='solid')
                    cell.font = Font(color='FFFFFF', bold=True)

                # Auto-adjust column widths
                for column in worksheet.columns:
                    max_length = 0
                    column = [cell for cell in column]
                    for cell in column:
                        try:
                            if len(str(cell.value)) > max_length:
                                max_length = len(str(cell.value))
                        except:
                            pass
                        adjusted_width = (max_length + 2)
                        worksheet.column_dimensions[column[0].column_letter].width = adjusted_width

            print(f"Excel file updated successfully at: {os.path.abspath(self.filename)}")
            return True
            
        except Exception as e:
            print(f"Error updating Excel file: {e}")
            return False