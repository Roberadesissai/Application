import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Buttons")
window.geometry("600x400")

# Buttons
def button1_func():
    print("Button 1 was pressed!")

button_string = tk.StringVar(value = 'A button with string var')
button1 = ttk.Button(master = window, text = "Button 1" , command = button1_func, textvariable = button_string)
button1.pack()


# checkbutton
check = ttk.Checkbutton(master = window, text = "Checkbutton")
check.pack()


# Run
window.mainloop()