import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def button_clicked():
    print('Button clicked')

def select(option):
    print(option)

button = ttk.Button(root, text="Click me", command=button_clicked)
button.pack()

ttk.Button(root, text='Rock', command=lambda: select('Rock')).pack()
ttk.Button(root, text='Paper',command=lambda: select('Paper')).pack()
ttk.Button(root, text='Scissors', command=lambda: select('Scissors')).pack()

root.mainloop()