
# JPG to PNG Converter

This Python script converts all images in a specified directory to PNG format and saves them in a target directory. It's a simple and efficient way to preprocess and standardize image files for further use.

## Features

- Converts images in any format to PNG.
- Automatically creates the target directory if it doesn't exist.
- Preserves the original filenames.

## Requirements

Make sure you have the necessary dependencies installed before running the script. You can install them using the `requirements.txt` file.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-repository-name.git

2. Navigate to the project directory:
    ```bash
    cd your-repository-name

3. Create and activate a virtual environment (recommended):

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `.\env\Scripts\activate`

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    
### Usage
To use this script, run it from the command line with the following syntax:

    python script_name.py <source_directory> <target_directory>
    <source_directory>: The directory containing the images you want to convert.
    <target_directory>: The directory where the converted PNG images will be saved.

### Example
    python convert_images.py ./images ./converted_images
This command will convert all images in the ./images directory to PNG format and save them in the ./converted_images directory. If the converted_images directory doesn't exist, the script will create it for you.

### Important Notes

Ensure the target directory (<target_directory>) is where you want your preprocessed (converted) files to be stored. If the directory already exists, make sure it either contains only files that you don't mind overwriting or is empty.
The script assumes the source directory contains valid image files that can be opened by the Pillow library.

### Contributing
If you'd like to contribute, feel free to fork the repository and submit a pull request. Issues and feature requests are welcome!
