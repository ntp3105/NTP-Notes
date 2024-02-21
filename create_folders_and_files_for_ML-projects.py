import os
import sys

folder_names = ['images','src','notebooks','data','models','deploy','config','tests']
file_names = ['README.md','LICENSE.txt','requirements.txt']

def create_folders_and_files(prj_path):
    """This function creates a series of folders and files of particular formats

    Args:
        folder_path (str): This inputs folder path as system argument, and creates path to add folders & files 
    """
    # Create folder path if it doesn't exist
    if not os.path.exists(prj_path):
        os.makedirs(prj_path)
    
    # Create folders
    for i in range(len(folder_names)):
        folder_name = folder_names[i]
        folder_path = os.path.join(prj_path, folder_name)
        os.makedirs(folder_path)
    print("Folders are created successfully.")
    
    # Create files
    for i in range(len(file_names)):
        file_name = file_names[i]
        file_path = os.path.join(prj_path, file_name)
        with open(file_path, 'w'):
            pass
    print("All files are created successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_folders_and_files.py <folder_path>")
        sys.exit(1)
    
    prj_path = sys.argv[1]
    create_folders_and_files(prj_path)
    print("The repository is set successfully. You are good to go for building awesome ML projects. Sky is the limit, bub!!!")
