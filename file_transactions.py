
class FileTransaction:
    def __init__(self):
        self.file_list = []
        self.directory = ''

    def update_file_list(self, file):
        self.file_list.append(file)

    def get_file_list(self):
        return self.file_list

    def update_directory(self, directory):
        self.directory = directory

    def get_directory(self):
        return self.directory

