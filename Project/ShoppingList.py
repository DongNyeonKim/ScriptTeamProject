import tkinter
import tkinter.ttk
import CrowlingShoppingList as CSL
from tkinter import *
import tkinter.ttk as ttk
import webbrowser as wbs

def cc():
    treeview.tag_configure("tag2", background="red")

def OnDoubleClick(e):
    #treeview에서 선택된 아이템정보 가져오기
    selectedItem = treeview.item(treeview.selection()[0])['values']
    # 0: name, 1: addr, 2: remain (주소와 판매처 이름 합치기)
    print(selectedItem)

    #wbs.open(selectedItem, new=1) #해당 주소로 인터넷창 팝업


def makeShoppingList(window):
    global treeview
    treeview = tkinter.ttk.Treeview(window, columns=["one", "two","three"], displaycolumns=["one", "two","three"],padding=10)
    treeview.place(x=450, y= 270)

    scrY = ttk.Scrollbar(orient='vertical', command=treeview.yview)
    scrY.place(x=1045, y=270, height=245)
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
        treeview.insert('', 'end', text=i+1, values=CSL.SearchList[i])

    treeview.tag_bind("tag1", sequence="<<TreeviewSelect>>", callback=cc)
    treeview.bind("<Double-1>", OnDoubleClick)