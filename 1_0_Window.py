import tkinter as tk
from tkinter import ttk

def button_func():
    print('A button was pressed!')

def exercise_button_func():
    print('Hello')

# Create a window
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x500")

# Create a label
label = ttk.Label(master = window, text="Window And Widgets!")
label.pack()

# Create a text entry widget
text = tk.Text(master = window)
text.pack()

# Create Entry widget
entry = ttk.Entry(master = window)
entry.pack()

# Exercise Label
exercise_label = ttk.Label(master = window, text = "My Label")
exercise_label.pack()

# Create a button widget
button = ttk.Button(master = window, text = 'A Button', command = button_func)
button.pack()

# Exercise Button
exercise_button = ttk.Button(master = window, text = 'Exercise Button', command = lambda: print('Exercise Button was pressed!'))
exercise_button.pack()










# RUN
window.mainloop()