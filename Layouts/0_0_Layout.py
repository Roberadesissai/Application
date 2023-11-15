import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry("600x400")
window.title("Layout intro")


# Widgets
label1 = ttk.Label(window, text = 'Label 1', background='red')
label2 = ttk.Label(window, text = 'Label 2', background='blue')

# pack
# label1.pack(side='left', expand=True, fill ='y')
# label2.pack(side='left')

# grid
# window.grid_columnconfigure(0, weight=1)
# window.grid_columnconfigure(1, weight=1)
# window.grid_columnconfigure(2, weight=2)
# window.rowconfigure(0, weight=1)

# label1.grid(row = 0, column = 1, sticky='n')

# place

label1.place(x=100, y=100)
label2.place(x=200, y=200)






# Run
window.mainloop()
