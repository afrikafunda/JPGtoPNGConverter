import sys
import os
from PIL import Image

# Get the source path of the images and the target directory from the command-line arguments
path = sys.argv[1]
directory = sys.argv[2]

# Check if the target directory exists; if not, create it.
# This is the directory where your processed files will be saved.
# Ensure that this directory is empty or contains only files that you are okay with being overwritten.
if not os.path.exists(directory):
    os.makedirs(directory)

# Iterate over each file in the source directory
for filename in os.listdir(path):
    # Extract the file name without the extension
    clean_name = os.path.splitext(filename)[0]
    
    # Open the image using Pillow
    img = Image.open(f'{path}{filename}')
    
    # Save the image in PNG format to the target directory
    # Ensure the file path has the correct format by adding a '/' between the directory and filename
    img.save(f'{directory}/{clean_name}.png', 'png')
    
    # Print a confirmation message for each processed file
    print('All done!!')

