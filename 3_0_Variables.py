import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('Hello World!')
# Window
window = tk.Tk()
window.title("Tkinter Variables")
window.geometry("300x150")


# tkinter variables
string_var = tk.StringVar()


# widgets
label = ttk.Label(master = window, text="Label", textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

button = ttk.Button(master = window, text = "Button", command = button_func)
button.pack()

# Run
window.mainloop()