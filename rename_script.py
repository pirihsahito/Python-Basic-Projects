import os

def format_directory_names(root_dir):
    """
    Traverses the directory tree from the bottom up, 
    replacing spaces with underscores in all files and folders.
    """
    # topdown=False ensures we rename contents of a folder before renaming the folder itself
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        
        # 1. Rename all files in the current directory
        for filename in filenames:
            if ' ' in filename:
                old_file_path = os.path.join(dirpath, filename)
                new_filename = filename.replace(' ', '_')
                new_file_path = os.path.join(dirpath, new_filename)
                
                os.rename(old_file_path, new_file_path)
                print(f"Renamed file: '{filename}' -> '{new_filename}'")

        # 2. Rename all subdirectories in the current directory
        for dirname in dirnames:
            if ' ' in dirname:
                old_dir_path = os.path.join(dirpath, dirname)
                new_dirname = dirname.replace(' ', '_')
                new_dir_path = os.path.join(dirpath, new_dirname)
                
                os.rename(old_dir_path, new_dir_path)
                print(f"Renamed folder: '{dirname}' -> '{new_dirname}'")

if __name__ == "__main__":
    # Define the absolute or relative path
    # Example for Windows: r"C:\Users\YourName\Documents\Your-Folder"
    # Example for Mac/Linux: "/home/username/Documents/Your-Folder"
    
    target_folder = r"YOUR_FOLDER_PATH_HERE" 
    
    if os.path.exists(target_folder):
        print(f"Scanning directory: {target_folder}\n")
        format_directory_names(target_folder)
        print("\nProcess completed successfully.")
    else:
        print("Error: The specified folder path does not exist. Please check the target_folder variable.")