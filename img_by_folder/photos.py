"""
This script is designed to help users organize their files by grouping them into subfolders
based on their date information, facilitating better file management.
"""

import os
import shutil
from datetime import datetime

# Prompt the user for the folder path
folder_path = input("Enter the folder path: ")

# Check if the specified path exists
if not os.path.exists(folder_path):
    print("The specified path does not exist.")
else:
    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Iterate through each file

    for filename in files:
        # Extract the prefix with `_` from the file name
        prefix = filename[:4] if filename[3] == '_' else filename[:5]
        try:
            # Extract the date from the file name and convert it to a datetime format
            date_str = filename[len(prefix):len(prefix) + 8]
            date_obj = datetime.strptime(date_str, "%Y%m%d")

            # Create a new folder with the date name if it doesn't already exist
            new_folder_name = date_obj.strftime("%Y-%m")
            new_folder_path = os.path.join(folder_path, new_folder_name)

            if not os.path.exists(new_folder_path):
                os.mkdir(new_folder_path)

            # Move the file to the new folder
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(new_folder_path, filename)
            shutil.move(old_file_path, new_file_path)

            print(f"Moved file {filename} to folder {new_folder_name}")
        except (ValueError, IndexError):
            print(f"Skipped file {filename}: invalid date format")

    print("Done.")
