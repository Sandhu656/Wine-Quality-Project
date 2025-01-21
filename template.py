import os
from pathlib import Path
import logging

# Configure logging to show detailed information
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Ensure no trailing spaces in project_name
project_name = "WineQualityPrediction"

# List of files to be created
list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]

# File and directory creation logic
for filepath in list_of_files:
    filepath = Path(filepath.strip())  # Remove trailing spaces
    filedir, filename = os.path.split(filepath)  # Split directory and file name

    # Create directory if it doesn't exist
    if filedir:
        try:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Directory created: {filedir}")
        except Exception as e:
            logging.error(f"Error creating directory {filedir}: {e}")

    # Create the file if it doesn't exist or is empty
    try:
        if not filepath.exists() or filepath.stat().st_size == 0:
            with open(filepath, "w") as f:
                pass  # Create an empty file
            logging.info(f"File created: {filepath}")
        else:
            logging.info(f"File already exists and is not empty: {filepath}")
    except Exception as e:
        logging.error(f"Error creating file {filepath}: {e}")
