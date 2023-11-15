import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry("600x400")
window.title("Pack")

# Widgets
label1 = ttk.Label(window, text = 'First label', background='red')
label2 = ttk.Label(window, text = 'Label 2', background='blue')
label3 = ttk.Label(window, text = 'Last of the labels', background='green')
button = ttk.Button(window, text = 'Button')

# layout
label1.pack(side='left', expand=True, fill ='x')
label2.pack(side='left')
label3.pack(side='right', expand=True, fill ='y')
button.pack(side='right')


# Run
window.mainloop()