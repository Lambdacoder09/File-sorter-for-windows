# File Organization Script

A Python script to organize files in a specified folder based on their file extensions. 📂📋

## Description

This script takes a folder path as input and organizes the files in that folder into separate folders based on their file extensions. It creates folders for each unique file extension and moves the corresponding files into their respective folders. 🗂️🔀

## Usage

1. Provide the path to the folder you want to organize by setting the `folder_path` variable in the script.
2. Run the script to organize the files in the specified folder.

## Requirements

- Python 3.x
- The `os` and `shutil` modules, which are part of the Python Standard Library.

## Usage Example

```python
import os
import shutil

def organize_files(folder_path):
    # Function implementation here...

# Provide the path to the folder you want to organize
folder_path = r"C:\Users\DELL\Downloads"
organize_files(folder_path)
