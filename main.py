import os
import tkinter as tk
from tkinter import messagebox as msg

from file_transactions import FileTransaction
from back_up_actions import BackUp

from showinfm import show_in_file_manager

home_directory = os.path.expanduser('~')

main_font = "Helvetica"
main_font_size = 14

Back_Up_Action = BackUp()
File_Transactions = FileTransaction()


def main():
    root = tk.Tk()
    root.title("Backer")
    root.geometry('800x600')
    """ THIS HIDES HIDDEN FILES FROM APPEARING IN THE FILE SELECTION WINDOWS """
    """ NOT MY CODE AND I DON'T KNOW HOW OR WHY IT WORKS """
    try:
        # call a dummy dialog with an impossible option to initialize the file
        # dialog without really getting a dialog window; this will throw a
        # TclError, so we need a try...except :
        try:
            root.tk.call('tk_getOpenFile', '-foobarbaz')
        except tk.TclError:
            pass
        # now set the magic variables accordingly
        root.tk.call('set', '::tk::dialog::file::showHiddenBtn', '1')
        root.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')
    except:
        pass
    """"""


    text_box = tk.Text(height=10)
    current_files_in_text_box(text_box)
    open_file_btn(root, text_box)
    back_up_directory_btn(root)
    back_up_btn(root)
    open_back_up_directory(root)
    delete_files_btn(root, text_box)
    text_box.pack()

    root.mainloop()

def ask_delete_files(text_box):
    response = msg.askyesnocancel(title="Delete Files", message="Are you sure you want to delete the backed up files?",
                                  detail="This action cannot be undone",
                                  icon=msg.WARNING)
    if response:
        Back_Up_Action.delete_backed_up_files(text_box)

def delete_files_btn(root, text_box):
    delete_btn = tk.Button(root, text='Delete Files', command=lambda: ask_delete_files(text_box))
    delete_btn.pack()

def current_files_in_text_box(text_box):
    files_list = File_Transactions.get_file_list()
    if files_list:
        for line in files_list['files']:
            file_name = line['file_path'].split('/')[-1]
            text_box.insert(tk.END, f'{file_name}: {line['date_created']}\n')

def open_file_btn(root, text_box):
    file_path_btn = tk.Button(root, text="Open File",
                              command= lambda: Back_Up_Action.get_file_address(root, home_directory, text_box))
    file_path_btn.pack()

def back_up_directory_btn(root):
    directory_path = tk.Button(root, text="Choose a Back Up Directory",
                               command=lambda: Back_Up_Action.get_directory_address(root, home_directory))
    directory_path.pack()

def back_up_btn(root):
    back_up = tk.Button(root, text="Back Up Files", command=Back_Up_Action.back_up)
    back_up.pack()

def open_back_up_directory(root):
    directory = File_Transactions.get_directory()
    btn = tk.Button(root, text="Open back up folder", command=lambda: show_in_file_manager(directory))
    btn.pack()



main()

