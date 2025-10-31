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
def open_file(root):
    global file
    global files
    file = fd.askopenfilename(parent=root, title='Open File', initialdir=home_directory)
    if file:
        files.append(file)

    f_label = tk.Label(text='')
    print(len(files))
    print(files)
    if len(files) >= 1:
        for f in files:
            file_name = f.split('/')[-1]
            f_label.config(text=file_name)
            f_label.pack()

def save_file(root):
    global save_directory
    save_directory = fd.askdirectory(parent=root, title='Save to', initialdir=home_directory)

def back_up(root):
    global files
    if len(files) > 0 and save_directory:
        for f in files:
            shutil.copy2(f, save_directory)
        success_msg = tk.Label(root, text="Back up completed!")
        success_msg.pack()
    else:
        warning_msg = msg.showwarning(title="Warning", message="Select a file and directory to save it")
        print("File not found")

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
    file_path_btn = tk.Button(root, text="Open File", command=lambda: open_file(root))
    file_path_btn.pack()

    # Save directory
    save_btn = tk.Button(root, text="Choose destination", command=lambda: save_file(root))
    save_btn.pack()

    # Back up files
    back_up_btn = tk.Button(root, text="Back Files", command=lambda: back_up(root))
    back_up_btn.pack()

    root.mainloop()

main()

