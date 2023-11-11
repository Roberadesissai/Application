import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Buttons")
window.geometry("600x400")

# Buttons
def button1_func():
    print("Button 1 was pressed!")
    print(radio_var.get())

button_string = tk.StringVar(value = 'A button with string var')
button1 = ttk.Button(master = window, text = "Button 1" , command = button1_func, textvariable = button_string)
button1.pack()


# checkbutton
check_var = tk.IntVar(value = 10)
check1 = ttk.Checkbutton(
    window,
    text = "Check 1",
    command = lambda: print(check_var.get()),
    variable = check_var, 
    onvalue = 10, 
    offvalue = 5
)
check1.pack()

check2 = ttk.Checkbutton(window, 
                         text = "Check 2", 
                         command = lambda: check_var.set(5))
    
check2.pack()

# radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton( window, 
                         text = "Radiobutton 1",
                         value = 'radio 1',
                         variable = radio_var,
                         command = lambda: print(radio_var.get()) )
radio1.pack()

radio2 = ttk.Radiobutton( window, 
                         text = "Radiobutton 2", 
                         value= 'radio 2', 

                         command = lambda: print(radio_var.get()) )
radio2.pack()


def radio_func():
    print(check_bool.get())
    check_bool.set(False)
    
# data   
radio_string = tk.StringVar()
check_bool = tk.BooleanVar()

# widgets
exerise_radio1 = ttk.Radiobutton( window, 
                                 text = 'Radio A', 
                                 value = 'A', 
                                 command = radio_func, 
                                 variable = radio_string)

exerise_radio2 = ttk.Radiobutton( window, 
                                 text = 'Radio B', 
                                 value = 'B', 
                                 command = radio_func,
                                 variable = radio_string)

exercise_check = ttk.Checkbutton( window, 
                                 text = 'Exercise check', 
                                 variable = check_bool,
                                 command = lambda: print(radio_string.get()))

exerise_radio1.pack()
exerise_radio2.pack()
exercise_check.pack()


# Run
window.mainloop()