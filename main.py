import os
import shutil

def organize_files(folder_path):
    # Create a dictionary to store folder names based on file extensions
    extensions = {}

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Iterate over each file
    for file_name in files:
        # Get the file extension
        _, file_extension = os.path.splitext(file_name)

        # Skip directories
        if os.path.isdir(os.path.join(folder_path, file_name)):
            continue

        # Create a folder for the extension if it doesn't exist
        if file_extension not in extensions:
            extension_folder = file_extension[1:]
            extensions[file_extension] = os.path.join(folder_path, extension_folder)
            os.makedirs(extensions[file_extension], exist_ok=True)

        # Move the file to the appropriate folder
        source_file = os.path.join(folder_path, file_name)
        destination_file = os.path.join(extensions[file_extension], file_name)
        shutil.move(source_file, destination_file)

    print("File organization completed.")

# Provide the path to the folder you want to organize
folder_path = r"C:\Users\DELL\Downloads"
organize_files(folder_path)
