import os
import shutil

file_path = "/home/leo-s-laptops/Documents/coding_projects/save_files_backer/example_file.txt"
destination = "/home/leo-s-laptops/Desktop"
isFile = os.path.isfile(file_path)

if isFile:
    shutil.copy2(file_path, destination)
else:
    raise FileNotFoundError("Enter valid path")