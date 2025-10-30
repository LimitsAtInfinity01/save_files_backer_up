import tkinter as tk

root = tk.Tk()
root.title("Hello World")
root.geometry('500x350')

def answer():
    # hidden_label.config(text="")
    hidden_label.config(text=f'You said your name is {entry.get()}')

def clear():
    hidden_label.config(text="")
    entry.delete(0, tk.END)

label = tk.Label(root, text="Enter your name", font=("", 24))
label.pack(pady=20)

entry = tk.Entry(root)
entry.pack(pady=20)

button = tk.Button(root, text="Answer", font=("", 18), command=answer)
button.pack()

hidden_label = tk.Label(root, text="", font=("", 18))
hidden_label.pack()

delete = tk.Button(root, text="Clear", font=("", 18), command=clear)
delete.pack()

root.mainloop()