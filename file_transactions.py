import os
import datetime
import json


class FileTransaction:
    def __init__(self):
        self.directory = ''
        self.data = {}
        self.current_files = None

    def update_file_list(self, file):
        created_at = datetime.datetime.now()
        current_files = None
        self.data = {
            "files":
            [
                {
                "file_path": file,
                "date_created": created_at.date()
                }
            ]
        }
        # read the JSON and load current files
        if os.path.getsize('file_json.json') != 0: # checks if file empty
            with open('file_json.json', 'r') as current_json:
                current_files = json.load(current_json)
                current_files["files"].append({
                    "file_path": file,
                    "date_created": created_at.date()
                })
            with open("file_json.json", "w") as json_file:
                json.dump(current_files, json_file, indent=4, default=str)
        else:
            # creates JSON
            with open("file_json.json", "w") as json_file:
                json.dump(self.data, json_file, indent=4, default=str)
                self.current_files = self.data

    @staticmethod
    def get_file_list():
        data = []
        if os.path.getsize('file_json.json') != 0:
            with open("file_json.json", 'r') as file:
                data = json.load(file)
                return data
        else:
            return data

    def update_directory(self, directory):
        self.directory = directory
        with open('back_up_directory.txt', 'w') as f:
            f.write(self.directory)

    def get_directory(self):
        with open('back_up_directory.txt', 'r') as f:
            directory = f.readline()
            if directory != '':
                self.directory = directory
        return self.directory

    @staticmethod
    def backed_up_files(file):
        with open('backed_up_files.txt', 'a') as f:
            f.write(file)


