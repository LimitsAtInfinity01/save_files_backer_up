import os
import shutil
import tkinter as tk
from tkinter import filedialog as fd

home_directory = os.path.expanduser('~')

root = tk.Tk()
root.title("Backer")
root.geometry('800x600')
main_font = "Helvetica"
main_font_size = 14

file = ''
save_directory = ''

""" NOT MY CODE AND I DON'T KNOW HOW OR WHY IT WORKS """
""" THIS HIDES HIDDEN FILES FROM APPEARING IN THE FILE SELECTION WINDOWS """
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

# tkinter.filedialog.askopenfile(mode='r', **options)
def open_file():
    global file
    file = fd.askopenfilename(parent=root, title='Open File', initialdir=home_directory)

def save_file():
    global save_directory
    save_directory = fd.askdirectory(parent=root, title='Save to', initialdir=home_directory)

def back_up():
    if file:
        if save_directory:
            shutil.copy2(file, save_directory)
        else:
            print("Wronged Directory")
    else:
        print("File not found")

    print("Back up completed!")
    truncated_file = file.split('/')[-1]
    print(f"File {truncated_file} was save to {save_directory}")

    success_msg = tk.Label(root, text="Back up completed!")
    success_path_saved_to = tk.Label(root, text=f"File {truncated_file} was save to {save_directory}")
    success_msg.pack()
    success_path_saved_to.pack()

# File Ope Button
file_path_btn = tk.Button(root, text="Open File", command=open_file)
file_path_btn.pack()

# Save directory
save_btn = tk.Button(root, text="Choose destination", command=save_file)
save_btn.pack()

# Back up files
back_up_btn = tk.Button(root, text="Back Files", command=back_up)
back_up_btn.pack()


root.mainloop()