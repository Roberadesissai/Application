import tkinter as tk
import ttkbootstrap as root

# Window
window = root.Window(themename = 'darkly')
window.title("Demo")
window.geometry("300x150")

# Label
label = root.Label(master = window, text="Miles to Kilometers Converter", font = ("Calibri", 15, "bold"))
label.pack()

def convert():
    miles = entry_into.get()
    kilometers = miles * 1.609
    output_string.set(f"{kilometers:.2f} km")


# input field
frame = tk.Frame(master = window)
entry_into = tk.IntVar()
entry = root.Entry(master = frame, textvariable = entry_into)

# button
button = root.Button(master = frame, text = "Convert", command = convert )
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
frame.pack(pady = 10)


# output field
output_string = tk.StringVar()
output_label = root.Label(master = window, text = "output", textvariable = output_string) 
output_label.pack(pady = 5)




# run
window.mainloop()