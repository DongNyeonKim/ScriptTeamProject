import tkinter
import tkinter.ttk
import CrowlingShoppingList as CSL
from tkinter import *
import tkinter.ttk as ttk

def cc():
    treeview.tag_configure("tag2", background="red")

def makeShoppingList(window):
    global treeview
    treeview = tkinter.ttk.Treeview(window, columns=["one", "two","three"], displaycolumns=["one", "two","three"],padding=5)
    treeview.place(x=450, y= 250)

    scrY = ttk.Scrollbar(orient='vertical', command=treeview.yview)
    scrY.place(x=724, y=220, height=335)
    treeview.config(yscrollcommand=scrY.set)

    treeview.column("#0", width=70)
    treeview.heading("#0", text="No")

    treeview.column("one", width=100, anchor="center")
    treeview.heading("one", text="인식표", anchor="center")

    treeview.column("two", width=300, anchor="center")
    treeview.heading("two", text="제품명", anchor="center")

    treeview.column("three", width=100, anchor="center")
    treeview.heading("three", text="가격", anchor="center")

    for i in range(len(CSL.SearchList)):
        treeview.insert('', 'end', text=i, values=CSL.SearchList[i])

    treeview.tag_bind("tag1", sequence="<<TreeviewSelect>>", callback=cc)
