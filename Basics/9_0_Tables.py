import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry("600x400")
window.title("reeview")

# data
first_names = ['Bob', 'Jane', 'John', 'Mary', 'Sue']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Davis']

# treeview
treeview = ttk.Treeview(window, columns = ('first', 'last', 'email'), show = 'headings')
treeview.heading('first', text = 'First Name')
treeview.heading('last', text = 'Surname')
treeview.heading('email', text = 'Email')
treeview.pack(fill = 'both', expand = 'yes')


# insert values into a table
# treeview.insert(parent = '', index = 0, values = ('John', 'Smith', 'hzdkv@example.com'))

# for i in range(len(first_names)):
#     treeview.insert(parent = '', index = 'end', values = (first_names[i], last_names[i], f'{first_names[i]}.{last_names[i]}@<EMAIL>'))

for i in range(10):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first}.{last}@gmail.com'
    data = (first, last, email)
    treeview.insert(parent = '', index = 'end', values = (first, last, email))
    
treeview.insert(parent = '', index = 1, values = ('ABCD', 'EFGH', 'IJKL@example.com'))

# event
def item_select(_):
    for i in treeview.selection():
        print(treeview.item(i, 'values'))
        
def delete_item(_):
    for i in treeview.selection():
        treeview.delete(i)
        
treeview.bind('<<TreeviewSelect>>', item_select)
treeview.bind('<Delete>', delete_item)




# Run
window.mainloop()