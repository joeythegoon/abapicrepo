import os
import shutil
import re

def copy_numeric_files_only(source_folder, destination_folder):
    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Regular expression for filenames with only digits
    number_only_pattern = re.compile(r'^\d+$')

    for filename in os.listdir(source_folder):
        name, ext = os.path.splitext(filename)
        if number_only_pattern.match(name):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)
            shutil.copy2(source_path, destination_path)
            print(f"Copied: {filename}")

# Example usage
source_dir = r"C:\Users\vent1\OneDrive\Desktop\New folder (3)\Battlers"
destination_dir = r"C:\Users\vent1\OneDrive\Desktop\New folder (3)\Battlers\Transfers"

copy_numeric_files_only(source_dir, destination_dir)
