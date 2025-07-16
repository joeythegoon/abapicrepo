import os
import shutil

# Set the path to the base folder that contains the subfolders
base_folder = "C:/Users/vent1/OneDrive/Desktop/New folder (3)/gen 2/SageDeoxys"  # <-- Change this to your actual folder path

# Create the 'rips' folder inside the base folder
rips_folder = os.path.join(base_folder, "rips")
os.makedirs(rips_folder, exist_ok=True)

# Iterate through each item in the base folder
for item in os.listdir(base_folder):
    subfolder_path = os.path.join(base_folder, item)
    
    if os.path.isdir(subfolder_path):
        front_png_path = os.path.join(subfolder_path, "Front.png")
        
        if os.path.isfile(front_png_path):
            # Convert folder name to lowercase for new file name
            new_file_name = f"{item.lower()}.png"
            destination_path = os.path.join(rips_folder, new_file_name)
            
            shutil.copy2(front_png_path, destination_path)
            print(f"Copied: {front_png_path} → {destination_path}")

print("Done.")
