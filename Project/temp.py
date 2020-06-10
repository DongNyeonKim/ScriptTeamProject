from tkinter import *
import tkinter.ttk as ttk
from tkinter import ttk
import json
from PIL import Image, ImageTk
okno = Tk()

def maketable():
       style = ttk.Style(okno)
       style.configure("TVS.Treeview", rowheight=40)
       tv = ttk.Treeview(okno, style="TVS.Treeview")

       tv['columns'] = ('LName', 'Pic')
       tv.heading("#0", text='Jméno', anchor='w')
       tv.column("#0", anchor="w", width=200)

       tv.heading('LName', text='Příjmení')
       tv.column('LName', anchor='center', width=200)

       tv.heading('Pic', text='Obrazek')
       tv.column('Pic', anchor='center', width=200)

       dbf = open("xxx.json", 'r')
       db = json.loads(dbf.read())

       for i in range(0, len(db)):
           root_pic1 = Image.open(db[i]["Pic"])
           root_pic2 = ImageTk.PhotoImage(root_pic1)
           tv.insert('', 'end', image=root_pic2, text=db[i]['Name'], values=(db[i]['LName']))


       tv.pack()


def main():
       okno.mainloop()

if __name__ == '__main__':
       maketable()
       main()