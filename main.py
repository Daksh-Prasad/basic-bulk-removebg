import os
from rembg import remove
from PIL import Image
import io

# Define input and output folders
input_folder = 'input_images'
output_folder = 'output_images'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

def remove_background_bulk(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            # Save as PNG to support transparency
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".png")
            
            with open(input_path, 'rb') as file:
                input_image = file.read()
            
            try:
                # Remove background completely
                removed_bg_data = remove(input_image)
                
                # Load the output image with transparent background
                output_image = Image.open(io.BytesIO(removed_bg_data)).convert("RGBA")
                
                # Save the background-removed image as PNG
                output_image.save(output_path, format="PNG")
                
                print(f"Processed: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    remove_background_bulk(input_folder, output_folder)

# Made by Daksh Prasad - https://github.com/Daksh-Prasad
