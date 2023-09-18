"""
This script is designed to help users organize their files by grouping them into subfolders
based on their date information, facilitating better file management.

Files such as (POCO X4 Pro):
  IMG_20230917_082434.jpg  - photo
  VID_20230917_071501.mp4  - video
  PANO_20230511_185250.jpg - panorama

Files such as (Realme 6, Redmi 5+):
  IMG20230917082434.jpg - photo, panorama
  VID20230917071501.mp4 - video
"""

import re
import os
import shutil
from datetime import datetime


def move_files(path):
    # Get the list of files and subfolders in the folder
    files_and_folders = os.listdir(path)

    # Filter only files (no subfolders)
    files = [f for f in files_and_folders if os.path.isfile(os.path.join(path, f))]

    pattern = r'^(IMG_|VID_|PANO_)(\d{8})_(\d{6}).(jpg|mp4)$'
    for filename in files:
        match = re.match(pattern, filename)
        if match:
            new_filename = match.group(1) + match.group(2) + "_" + match.group(3) + "." + match.group(4)
            print(new_filename)
            try:
                # Extract the date from the file name and convert it to a datetime format
                date_obj = datetime.strptime(match.group(2), "%Y%m%d")

                # Create a new folder with the date name if it doesn't already exist
                new_folder_name = date_obj.strftime("%Y-%m")
                new_folder_path = os.path.join(path, new_folder_name)

                if not os.path.exists(new_folder_path):
                    os.mkdir(new_folder_path)

                # Move the file to the new folder
                old_file_path = os.path.join(path, new_filename)
                new_file_path = os.path.join(new_folder_path, new_filename)
                shutil.move(old_file_path, new_file_path)

                print(f"Moved file {new_filename} to folder {new_folder_name}")
            except (ValueError, IndexError):
                print(f"Skipped file {new_filename}: invalid date format")


def rename_files(path):
    # Get the list of files and subfolders in the folder
    files_and_folders = os.listdir(path)

    # Filter only files (no subfolders)
    files = [f for f in files_and_folders if os.path.isfile(os.path.join(path, f))]

    pattern = r'^(IMG|VID)(\d{8})(\d{6}).(jpg|mp4)$'
    for filename in files:
        match = re.match(pattern, filename)
        if match:
            new_filename = match.group(1) + "_" + match.group(2) + "_" + match.group(3) + "." + match.group(4)

            old_file_path = os.path.join(path, filename)
            new_file_path = os.path.join(path, new_filename)

            os.rename(old_file_path, new_file_path)
            print(f"Renamed {filename} to {new_filename}")


if __name__ == "__main__":
    # Prompt the user for the folder path
    folder_path = input("Enter the folder path: ")

    # Check if the specified path exists
    if not os.path.exists(folder_path):
        print("The specified path does not exist.")
    else:
        rename_files(folder_path)
        move_files(folder_path)

        print("Done!")
