import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# List of project files to create
list_of_files = [
    "src/__init__.py", 
    "src/helper.py",
    ".env",
    "setup.py",
    "app.py",
    "prompt.py",
    "research/trials.ipynb",
    "README.md",
    "LICENSE",
    "template.py",
    "test.py",

]

# Loop to create folders and files
for filepath in list_of_files:
    filedir, filename = os.path.split(filepath)  # Separate file path and file name

    # Create directories if they do not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create the file if it doesn't exist or is empty
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass  # Creates an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

