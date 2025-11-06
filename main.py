import os
import tkinter as tk

from file_transactions import FileTransaction
from back_up_actions import BackUp

home_directory = os.path.expanduser('~')

main_font = "Helvetica"
main_font_size = 14

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
    Back_Up_Action = BackUp()

    # Gets the file after choosing by pressing the button
    file_path_btn = tk.Button(root, text="Open File",
                              command=lambda:
                              Back_Up_Action.get_file_address(root, home_directory)
                              )
    file_path_btn.pack()

    # Gets the target directory to back up files
    directory_path = tk.Button(root,
                               text="Choose a Back Up Directory",
                               command=lambda:
                               Back_Up_Action.get_directory_address(root, home_directory)
                               )
    directory_path.pack()

    # Back up files
    back_up_btn = tk.Button(root,
                            text="Back Up Files",
                            command=Back_Up_Action.back_up
                            )
    back_up_btn.pack()

    root.mainloop()
main()

