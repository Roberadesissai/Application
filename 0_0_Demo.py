import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Demo")
window.geometry("300x150")

# Label
label = ttk.Label(master = window, text="Miles to Kilometers Converter", font = ("Calibri", 15, "bold"))
label.pack()


# input field
frame = tk.Frame(master = window)
entry = ttk.Entry(master = frame)

# button
button = ttk.Button(master = frame, text = "Convert")
entry.pack()
button.pack()
frame.pack()






# run
window.mainloop()