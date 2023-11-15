import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry("600x400")
window.title("Frames and parenting")

# frames

frame = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame.pack_propagate(False)
frame.pack()

# master setting
label = ttk.Label(frame, text = 'Label in a frame')
label.pack()

button = ttk.Button(frame, text = 'Button in a frame')
button.pack()

# example
label2 = ttk.Label(window, text = 'Label in a window')
label2.pack()




# Run
window.mainloop()