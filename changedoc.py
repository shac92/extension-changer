import os

def rename_files(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)

    for filename in files:
        # Check if the file has the .jpg_ extension
        if filename.endswith('.jpg_'):
                                #^This will be what the script looks for change it to what you need it to look for.
            # Generate the new filename by replacing .jpg with .jpeg
            new_filename = filename.replace('.jpg_', '.jpeg')
                                            #^change these^ to the old extention type and the new extention type.
            # Rename the file
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

# Specify the folder path where the files are located
folder_path = '*insert new folder path here'

# Call the function to rename the files
rename_files(folder_path)
