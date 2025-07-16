from PIL import Image
import os

def downscale_images_by_half_to_drop(source_folder):
    drop_folder = os.path.join(source_folder, 'drop')
    os.makedirs(drop_folder, exist_ok=True)

    for filename in os.listdir(source_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.webp', '.bmp')):
            source_path = os.path.join(source_folder, filename)
            image = Image.open(source_path)

            new_width = image.width // 2
            new_height = image.height // 2
            resized_image = image.resize((new_width, new_height), Image.LANCZOS)

            dest_path = os.path.join(drop_folder, filename)
            resized_image.save(dest_path)
            print(f"Saved downscaled: {filename} -> drop/{filename}")

# Example usage
folder = r"C:\Users\vent1\OneDrive\Desktop\New folder (3)\Battlers\Transfers"
downscale_images_by_half_to_drop(folder)
