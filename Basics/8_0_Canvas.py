import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry("600x400")
window.title("Canvas")

# canvas
canvas = tk.Canvas(window, bg = 'white')
canvas.pack()

# canvas.create_rectangle(left, top, right, bottom)
# canvas.create_rectangle(50, 20, 100, 200, fill = 'blue', outline = 'black')
# canvas.create_oval(50, 20, 100, 200)
# canvas.create_line(50, 20, 100, 200)
# canvas.create_polygon(50, 20, 100, 20, 300, 100)
# canvas.create_arc((200, 0, 300, 100), fill = 'blue', outline = 'black', start = 45, extent = 180)

# canvas.create_text(100, 200, text = 'Hello World!')
# canvas.create_window((150,100), window = ttk.Button(window, text = 'Hello World!'))

def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval(x-brush_size / 2, y-brush_size / 2, x + brush_size / 2, y + brush_size / 2)
    
brush_size = 4
canvas.bind('<Motion>', draw_on_canvas)

# Run
window.mainloop()