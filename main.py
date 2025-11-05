import os
import shutil


import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as msg

home_directory = os.path.expanduser('~')
main_font = "Helvetica"
main_font_size = 14

file = ''
save_directory = ''
files = []

# It opens a file and adds it to the list of files to be copied
def open_file_to_back_up(root):
    global file
    global files

    list_of_files = gets_list_of_files_backed_up()
    if list_of_files:
        files = list_of_files

    file = fd.askopenfilename(parent=root, title='Open File', initialdir=home_directory)
    if file:
        files.append(file)

    # cleans the list of files and adds new files to the list
    f_label = tk.Label(text='')
    if len(files) >= 1:
        for f in files:
            file_name = f.split('/')[-1]
            f_label.config(text=file_name)
            f_label.pack()

# gets the directory where the files will be back up
def directory_to_back_up(root):
    global save_directory
    save_directory = fd.askdirectory(parent=root, title='Save to', initialdir=home_directory)
    saves_back_up_directory(save_directory)

# proceeds to back up files
def proceed_to_back_up(root):
    global files
    global save_directory
    files_to_back_up = gets_list_of_files_backed_up()
    back_up_directory = gets_back_up_directory()
    if files_to_back_up:
        files = files_to_back_up

    if back_up_directory:
        save_directory = back_up_directory

    if len(files) > 0 and save_directory:
        for f in files:
            shutil.copy2(f, save_directory)
        saves_list_of_files_backed_up(files)
        success_msg = tk.Label(root, text="Back up completed!")
        success_msg.pack()
    else:
        warning_msg = msg.showwarning(title="Warning", message="Select a file and directory to save it")
        print("File not found")

def saves_list_of_files_backed_up(files_list):
    with open('files.txt', 'a') as f:
        for item in files_list:
            f.write(f'{item}\n')

def gets_list_of_files_backed_up():
    list_of_files = []
    with open('files.txt', 'r') as f:
        for line in f:
            list_of_files.append(line.rstrip())
    return list_of_files

def saves_back_up_directory(directory):
    with open('back_up_directory.txt', 'w') as f:
        f.write(directory)

def gets_back_up_directory():
    with open('back_up_directory.txt', 'r') as f:
        directory = f.readline()
    return directory

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

    # File Ope Button
    file_path_btn = tk.Button(root, text="Open File", command=lambda: open_file_to_back_up(root))
    file_path_btn.pack()

    # Save directory
    save_btn = tk.Button(root, text="Choose destination", command=lambda: directory_to_back_up(root))
    save_btn.pack()

    # Back up files
    back_up_btn = tk.Button(root, text="Back Up Files", command=lambda: proceed_to_back_up(root))
    back_up_btn.pack()


    files_to_display = gets_list_of_files_backed_up()
    if files_to_display:
        for f in files_to_display:
            file_name = f.split('/')[-1]
            f_label = tk.Label(text=file_name)
            f_label.pack()

    root.mainloop()

main()

