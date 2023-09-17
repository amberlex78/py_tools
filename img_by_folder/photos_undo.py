"""
This script is designed to organize files in a folder by moving them into subfolders
based on their date information in the filename.
"""

import os
import shutil

# Prompt the user for the folder path
folder_path = input("Enter the folder path: ")

# Check if the specified path exists
if not os.path.exists(folder_path):
    print("The specified path does not exist.")
else:
    # Get a list of subfolders in the folder

    # Before refactoring:
    """
    subfolders = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            subfolders.append(item)
    """

    # After refactoring
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

    # Iterate through each subfolder
    for subfolder in subfolders:
        subfolder_path = os.path.join(folder_path, subfolder)

        # Get the list of files in the subfolder
        files = os.listdir(subfolder_path)

        # Iterate through each file
        for filename in files:
            file_path = os.path.join(subfolder_path, filename)

            # Move the file back to the original folder
            new_file_path = os.path.join(folder_path, filename)
            shutil.move(file_path, new_file_path)

            print(f"Moved file {filename} from folder {subfolder} to the original folder")

        # Remove the empty subfolder
        os.rmdir(subfolder_path)

    print("Done.")
