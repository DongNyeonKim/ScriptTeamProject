import tkinter
import tkinter.ttk
import CrowlingShoppingList as CSL
from tkinter import *
import tkinter.ttk as ttk
import webbrowser as wbs
from io import BytesIO
from PIL import Image, ImageTk
import urllib.request

def giveImageURL(e):
    imageURL = treeview.item(treeview.selection())['values'][4]
    print(imageURL)
    with urllib.request.urlopen(imageURL) as u:
        global newImg2
        raw_data = u.read()
        im = Image.open(BytesIO(raw_data))
        im = im.resize((250, 250), Image.ANTIALIAS)
        newImg2 = ImageTk.PhotoImage(im)
        imageLabel.configure(image=newImg2)


def OnDoubleClick(e):
    #treeview에서 선택된 아이템정보 가져오기
    selectedItem = treeview.item(treeview.selection()[0])['values'][3]

    wbs.open(selectedItem, new=1) #해당 주소로 인터넷창 팝업


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

    global imageLabel
    imageLabel = Label(window, background = "LightSteelBlue1")
    imageLabel.place(x=100,y=150)

    treeview.bind("<ButtonRelease-1>", giveImageURL)
    treeview.bind("<Double-1>", OnDoubleClick)