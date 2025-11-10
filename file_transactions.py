import datetime

class FileTransaction:
    def __init__(self):
        self.file_list = []
        self.directory = ''
        self.file_dict = {}

    def update_file_list(self, file):
        if file not in self.file_list:
            self.file_list.append(file)

            created_at = datetime.datetime.now()
            self.file_dict['file_path'] = file
            self.file_dict['date_created'] = created_at

        print(self.get_dict_file())
        current_files = []
        with open('files_paths.txt', 'r') as r:
            for line in r:
                current_files.append(line.strip())

        with open('files_paths.txt', 'a') as f:
            for file in self.file_list:
                if file not in current_files:
                    f.write(f"{file}\n")

    def get_dict_file(self):
        return self.file_dict


    def get_file_list(self):
        with open('files_paths.txt', 'r') as f:
            for line in f:
                self.file_list.append(line.strip())
        return self.file_list

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

