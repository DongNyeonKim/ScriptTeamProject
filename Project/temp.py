import tkinter as tk
from tkinter import ttk

counter = 0
numbers = ['1', '10', '11', '2', '3', '4', '24', '12', '5']

def sort_treeview():
       content = [(tv.set(child, column), child)
                                   for child in tv.get_children('')]
       try:
           content.sort(key=lambda t: int(t[0]))
       except:
           content.sort()
       for index, (val, child) in enumerate(content):
           tv.move(child, '', index)

def add_item():
       global counter
       if counter < 8:
           tv.insert('', 'end', values=numbers[counter])
           counter += 1
           # Sort the treeview after the new item was inserted
           # -------------------------------------------------
           sort_treeview()

root = tk.Tk()
column = 'number'
tv = ttk.Treeview(root, columns=column, show='headings')
tv.pack()

button = tk.Button(root, text='Add entry', command=add_item)
button.pack()

root.mainloop()