import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# window
window = tk.Tk()
window.title("Sliders")

# slider
scale_float = tk.IntVar(value = 15)
scale = ttk.Scale(window, 
                  command = lambda value: print(scale_float.get()),
                  from_ = 0, 
                  to = 25, 
                  length = 200, 
                  orient = 'vertical',
                  variable= scale_float
                  )
scale.pack()


# progress bar
progress = ttk.Progressbar(window, length = 200, mode = 'determinate', variable = scale_float, maximum = 25)
progress.pack()


scrolled_text = scrolledtext.ScrolledText(window, width = 100, height = 5, wrap = tk.WORD)
scrolled_text.pack()


exercise_int = tk.IntVar()
exercise_progress = ttk.Progressbar(window, orient= 'vertical', variable=exercise_int)
exercise_progress.pack()
exercise_progress.start()

label = ttk.Label(window, textvariable= exercise_int)
label.pack()

exercise_scale = ttk.Scale(window, variable=exercise_int, from_ = 0, to = 100, length = 200)
exercise_scale.pack()



# Run
window.mainloop()