import os
from PIL import Image

# Source and destination paths
source_folder = "E:/Project/kidney stone prediction/images/CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/Stone"
destination_folder = "E:/Project/kidney stone prediction/images/CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/stone_vertical"

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through files in the source folder
for filename in os.listdir(source_folder):
    filepath = os.path.join(source_folder, filename)
    if os.path.isfile(filepath):
        try:
            # Open the image
            img = Image.open(filepath)
            # Check if the image dimensions are not 512x512
            if img.width != 512 or img.height != 512:
                # Save the image to the destination folder
                img.save(os.path.join(destination_folder, filename))
        except Exception as e:
            print(f"Error processing {filename}: {e}")
