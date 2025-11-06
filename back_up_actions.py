import shutil
from tkinter import filedialog as fd
from tkinter import messagebox as msg

class BackUp:
    def __init__(self):
        self.file = ''
        self.directory = ''
        self.files_list = []

    def get_file_address(self, root, home_directory):
        self.file = fd.askopenfilename(parent=root, title='Open File', initialdir=home_directory)
        self.files_list.append(self.file)

    def get_directory_address(self, root, home_directory):
        self.directory = fd.askdirectory(parent=root, title='Save to', initialdir=home_directory)
        print(self.directory)

    def get_file_list(self):
        return self.files_list

    def back_up(self):
        for file in self.files_list:
            shutil.copy2(file, self.directory)

    def __str__(self):
        return f'The files are {self.files_list} and the back up directory is {self.directory}'