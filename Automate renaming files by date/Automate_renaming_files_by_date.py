import os
import re
from datetime import datetime

def rename_files(directory):
    for filename in os.listdir(directory):
        # Search for date format dd-mm-yyyy or dd-Mmm-yyyy or dd-Mmmm-yyyy
        date_search = re.search(r'\b(\d{1,2}-\d{1,2}-\d{4})\b|\b(\d{1,2}-\w{3,}-\d{4})\b', filename)
        if date_search:
            date_str = date_search.group()
            # Determine date format
            date_format = '%d-%m-%Y' if date_str.replace('-', '').isdigit() else ('%d-%b-%Y' if len(date_str.split('-')[1]) == 3 else '%d-%B-%Y')
            # Convert date to dd-mm-yyyy format
            date = datetime.strptime(date_str, date_format)
            new_filename = 'Report ' + date.strftime('%d-%m-%Y')
            # Rename file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

# Ask the user for the directory path
directory_path = input("Please enter the directory path: ")
# Call the function with the user's directory path
rename_files(directory_path)
