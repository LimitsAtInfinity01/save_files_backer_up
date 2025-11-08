import shutil
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as msg

from file_transactions import FileTransaction

File_Transaction = FileTransaction()


class BackUp:
    def __init__(self):
        self.file = ''
        self.directory = ''
        self.backed_up_files = []

    def get_file_address(self, root, home_directory, text_box):
        self.file = fd.askopenfilename(parent=root, title='Open File', initialdir=home_directory)
        if not isinstance(self.file, tuple) and self.file != '':
            File_Transaction.update_file_list(self.file)

            file_set = set()
            for f in File_Transaction.get_file_list():
                file_set.add(f)

            text_box.delete("1.0", tk.END)
            for line in file_set:
                text_box.insert(tk.END, f'{line}\n')

    def get_directory_address(self, root, home_directory):
        self.directory = fd.askdirectory(parent=root, title='Save to', initialdir=home_directory)
        if not isinstance(self.directory, tuple) and self.file != '':
            File_Transaction.update_directory(self.directory)

    def back_up(self):
        files_list = File_Transaction.get_file_list()
        directory = File_Transaction.get_directory()
        success = False
        if directory:
            for f in files_list:
                shutil.copy2(f, directory)
                self.backed_up_files.append(f)
                success = True
        else:
            success = False
        if success:
            success_msg = msg.showinfo(message="Files Successfully Backed Up!")
        else:
            failed_msg = msg.showerror(message="Select files and destination first")



