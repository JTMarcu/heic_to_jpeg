import os
from PIL import Image
import pillow_heif

pillow_heif.register_heif_opener()  # <-- Add this line

input_folder = "heic_pics"
output_folder = "jpeg_pics"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".heic"):
        heic_path = os.path.join(input_folder, filename)
        jpeg_filename = os.path.splitext(filename)[0] + ".jpg"
        jpeg_path = os.path.join(output_folder, jpeg_filename)

        image = Image.open(heic_path)
        image.save(jpeg_path, "JPEG")
        print(f"Converted {filename} to {jpeg_filename}")
