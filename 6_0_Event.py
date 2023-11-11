import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'X: {event.x}, Y: {event.y}')

# Window
window = tk.Tk()
window.geometry("600x500")
window.title("Event Binding")

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text = "A button") 
btn.pack()

# events
window.bind('<Alt-KeyPress-a>', lambda event: print(enent))
text.bind('<Motion>', get_pos)

window.bind('<KeyPress>', lambda event: print(f'a button pressed ({event.char})'))

entry.bind('<FocusIn>', lambda event: print('Entry field was selected'))
entry.bind('<FocusOut>', lambda event: print('Entry field was deselected'))
text.bind('<Shift-MouseWheel>', lambda event: print('Mouse wheel moved'))

# Run
window.mainloop()