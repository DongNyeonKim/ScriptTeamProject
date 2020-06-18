from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
import tkinter.messagebox
import HomeUI
import ShoppingUI
import CoronaMaskList
import GetCoronaMap

def MoveHomeState():
    window.destroy()
    HomeUI.HomeState()

def MoveShoppingState():
    window.destroy()
    ShoppingUI.ShoppingState()

def titleImage():
    title_label = Label(window)
    title_label.image = PhotoImage(file = "리소스/코로나종합상황센터.PNG")
    title_label['image'] = title_label.image
    title_label.place(x=20,y=10)




def homeButton():
    home_Button =Button(window)
    pil_image = Image.open('리소스/홈버튼.JPG')
    pil_image = pil_image.resize((90, 90), Image.ANTIALIAS)
    home_Button.image = ImageTk.PhotoImage(pil_image)
    home_Button = Button(image = home_Button.image, command=lambda: MoveHomeState())
    home_Button.place(x=700,y=10)
    home_text = Label(window)
    home_text.place(x=735, y=110)
    home_text.configure(background='LightSteelBlue1')
    home_Button.bind("<Enter>", lambda _: home_text.configure(text="홈"))
    home_Button.bind("<Leave>", lambda _: home_text.configure(text=""))

def maskButton():
    mask_Button =Button(window)
    pil_image = Image.open('리소스/마스크아이콘.PNG')
    pil_image = pil_image.resize((90, 90), Image.ANTIALIAS)
    mask_Button.image = ImageTk.PhotoImage(pil_image)
    mask_Button = Button(image = mask_Button.image)
    mask_Button.place(x=800,y=10)
    mask_text = Label(window)
    mask_text.place(x=800, y=110)
    mask_text.configure(background='LightSteelBlue1')
    mask_Button.bind("<Enter>", lambda _: mask_text.configure(text="공적마스크 검색"))
    mask_Button.bind("<Leave>", lambda _: mask_text.configure(text=""))

def shoppingButton():
    shopping_Button =Button(window)
    pil_image = Image.open('리소스/쇼핑아이콘.PNG')
    pil_image = pil_image.resize((90, 90), Image.ANTIALIAS)
    shopping_Button.image = ImageTk.PhotoImage(pil_image)
    shopping_Button = Button(image = shopping_Button.image, command=lambda: MoveShoppingState())
    shopping_Button.place(x=900,y=10)
    shopping_text = Label(window)
    shopping_text.place(x=905, y=110)
    shopping_text.configure(background='LightSteelBlue1')
    shopping_Button.bind("<Enter>", lambda _: shopping_text.configure(text="방역물품 쇼핑"))
    shopping_Button.bind("<Leave>", lambda _: shopping_text.configure(text=""))

def telegramButton():
    telegram_Button =Button(window)
    pil_image = Image.open('리소스/텔레그렘아이콘.PNG')
    pil_image = pil_image.resize((90, 90), Image.ANTIALIAS)
    telegram_Button.image = ImageTk.PhotoImage(pil_image)
    telegram_Button = Button(image = telegram_Button.image)
    telegram_Button.place(x=1000,y=10)
    telegram_text = Label(window)
    telegram_text.place(x=1010, y=110)
    telegram_text.configure(background='LightSteelBlue1')
    telegram_Button.bind("<Enter>", lambda _: telegram_text.configure(text="텔레그렘 봇"))
    telegram_Button.bind("<Leave>", lambda _: telegram_text.configure(text=""))

def totalmapButton():
    totalmapButton =Button(window)
    pil_image = Image.open('리소스/지도.jpeg')
    pil_image = pil_image.resize((150, 150), Image.ANTIALIAS)
    totalmapButton.image = ImageTk.PhotoImage(pil_image)
    totalmapButton = Button(image = totalmapButton.image, command=lambda: GetCoronaMap.openTotalMap())
    totalmapButton.place(x=850,y=150)
    label = Label(window, text="전국 공적마스크 판매처")
    label.place(x=820, y=320)
    label.configure(foreground='black', background='LightSteelBlue1', font=('서울서체', 15, 'bold'))


def searchmapButton():
    searchmapButton =Button(window)
    pil_image = Image.open('리소스/지도.jpeg')
    pil_image = pil_image.resize((150, 150), Image.ANTIALIAS)
    searchmapButton.image = ImageTk.PhotoImage(pil_image)
    searchmapButton = Button(image = searchmapButton.image, command=lambda: GetCoronaMap.makeSearchMapData())
    searchmapButton.place(x=850,y=380)
    label = Label(window, text="검색 공적마스크 판매처")
    label.place(x=820, y=550)
    label.configure(foreground='black', background='LightSteelBlue1', font=('서울서체', 15, 'bold'))



def MaskState():
    global window
    window = Tk()
    window.title("Covid-19 ControlCenter")
    window.geometry("1100x600+100+100")
    window.configure(background='LightSteelBlue1')
    window.resizable(0, 0)  # 창 크기 고정

    homeButton()
    maskButton()
    shoppingButton()
    titleImage()
    telegramButton()
    CoronaMaskList.makeMaskList(window)

    totalmapButton()
    searchmapButton()
    window.mainloop()

