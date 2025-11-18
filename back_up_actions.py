import os.path
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
        self.current_path = ''

    def get_file_address(self, root, home_directory, text_box):
        if not self.current_path:
            self.file = fd.askopenfilename(parent=root, title='Open File', initialdir=home_directory)
        else:
            address = self.file.split('/')
            string_address = "/".join(item for item in address[:-1])
            print(f"{string_address}/")
            self.current_path = f"{string_address}/"
            self.file = fd.askopenfilename(parent=root, title='Open File', initialdir=self.current_path)


        if not isinstance(self.file, tuple) and self.file != '':
            File_Transaction.update_file_list(self.file)
            self.current_path = self.file
            file_set = set()
            files_list = File_Transaction.get_file_list()
            for line in files_list['files']:
                file_name = line['file_path'].split('/')[-1]
                file_set.add(f'{file_name}: {line['date_created']}\n')

            text_box.delete("1.0", tk.END)
            for line in file_set:
                text_box.insert(tk.END, line)

    def get_directory_address(self, root, home_directory):
        self.directory = fd.askdirectory(parent=root, title='Save to', initialdir=home_directory)
        full_path = f'{self.directory}/back_up'
        os.makedirs(full_path, exist_ok=True)
        if not isinstance(self.directory, tuple) and self.file != '':
            File_Transaction.update_directory(full_path)

    @staticmethod
    def back_up():
        files_list = File_Transaction.get_file_list()
        directory = File_Transaction.get_directory()
        success = False
        if directory:
            for file in files_list['files']:
                file_name = file['file_path'].split('/')[-1]
                shutil.copy2(file['file_path'], directory)
                File_Transaction.backed_up_files(f'{directory}/{file_name}\n') # creates a list of backed up files
                success = True
        else:
            success = False
        if success:
            success_msg = msg.showinfo(message="Files Successfully Backed Up!")
        else:
            failed_msg = msg.showerror(message="Select files and destination first")

    @staticmethod
    def delete_backed_up_files(text_box):
        deleted = False
        with open('backed_up_files.txt', 'r') as files:
            for file in files:
                print(f'File: {file.strip()}, deleted ...')
                try:
                    os.remove(file.strip())
                    deleted = True
                except FileNotFoundError:
                    failed_msg = msg.showerror(message="There is no files to delete")
        if deleted:
            open("backed_up_files.txt", "w").close()
            open("file_json.json", "w").close()
            text_box.delete("1.0", tk.END)
