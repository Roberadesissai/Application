import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Sliders")

# slider
scale = ttk.Scale(window, command = lambda value: print(value))
scale.pack()






# Run
window.mainloop()