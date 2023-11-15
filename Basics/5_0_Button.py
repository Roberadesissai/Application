import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk


def button_func(entry_string):
    print('a button was pressed!')
    print(entry_string.get())
    
def outer_func(parameter):
    def inner_func():
        print('a button was pressed!')
        print(parameter.get())
    return inner_func

# setup
window = tk.Tk()
window.title("Button,Function adn Agreement")

# widgets
entry_string = tk.StringVar(value = 'test')
entry = tk.Entry(window, textvariable = entry_string)
entry.pack()

button = ttk.Button(window, text = "Button", command = outer_func(entry_string))
button.pack()



# Run
window.mainloop()