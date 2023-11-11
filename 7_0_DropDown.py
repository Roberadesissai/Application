import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry("600x400")
window.title("Compo and Spin")

# combobox
items = ('Ice cream', 'Chocolate', 'Vanilla', 'Strawberry')
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable = food_string)
combo['values'] = items
# combo.configure(value = items)
combo.pack()

# event
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text = f'Selected value: {food_string.get()}'))

combo_label = ttk.Label(window, text = 'Selected value: ')
combo_label.pack()

# spinbox
spin_int = tk.IntVar(value = 12)
spin = ttk.Spinbox(window, 
                   from_ = 3, 
                   to = 20, 
                   increment = 1, 
                   command = lambda: print(spin_int.get()),
                   textvariable = spin_int)
                
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
spin.pack()


exercise_letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
exercise_string = tk.StringVar(value = exercise_letters[0])
exercise_spin = ttk.Spinbox(window, textvariable = exercise_string, value = exercise_letters) 
exercise_spin.pack()

exercise_spin.bind('<<Decrement>>', lambda event: print(exercise_string.get()))



# Run
window.mainloop()