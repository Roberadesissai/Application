import tkinter as tk
from tkinter import ttk


def button_func():
    # get the value from the entry widget
    print(entry.get())

    # update the label
    # label.config(text = entry.get())
    label['text'] = entry.get()
    entry['state'] = 'disabled'

def button_func_2():
    # get the value from the entry widget
    print(entry.get())
    
    # update the label
    # label.config(text = entry.get())
    label['text'] = 'Information'
    entry['state'] = 'enabled'
    entry.delete(0, tk.END)



# Create a window
window = tk.Tk()
window.title("Getting and Setting widgets")
window.geometry("300x150")

# Create a Widget
label = ttk.Label(master = window, text="Information")
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'Get', command = button_func)
button.pack()

button2 = ttk.Button(master = window, text = 'Set', command = button_func_2)
button2.pack()



# Run
window.mainloop()


