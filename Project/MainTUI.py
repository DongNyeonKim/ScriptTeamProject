from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
import tkinter.messagebox

window = Tk()
window.title("Covid-19 ControlCenter")
window.geometry("1100x600")

def titleImage():
    title_label = Label(window)
    title_label.image = PhotoImage(file = "리소스/코로나종합상황센터.PNG")
    title_label['image'] = title_label.image
    title_label.place(x=20,y=10)


def clickicon():
    print("Click")


def homeButton():
    home_Button =Button(window)
    pil_image = Image.open('리소스/홈버튼.JPG')
    pil_image = pil_image.resize((90, 90), Image.ANTIALIAS)
    home_Button.image = ImageTk.PhotoImage(pil_image)
    home_Button = Button(image = home_Button.image, command=lambda: clickicon())
    home_Button.place(x=700,y=10)
    home_text = Label(window)
    home_text.place(x=735, y=110)
    home_Button.bind("<Enter>", lambda _: home_text.configure(text="홈"))
    home_Button.bind("<Leave>", lambda _: home_text.configure(text=""))

def maskButton():
    mask_Button =Button(window)
    pil_image = Image.open('리소스/마스크아이콘.PNG')
    pil_image = pil_image.resize((90, 90), Image.ANTIALIAS)
    mask_Button.image = ImageTk.PhotoImage(pil_image)
    mask_Button = Button(image = mask_Button.image, command=lambda: clickicon())
    mask_Button.place(x=800,y=10)
    mask_text = Label(window)
    mask_text.place(x=800, y=110)
    mask_Button.bind("<Enter>", lambda _: mask_text.configure(text="공적마스크 검색"))
    mask_Button.bind("<Leave>", lambda _: mask_text.configure(text=""))

def shoppingButton():
    shopping_Button =Button(window)
    pil_image = Image.open('리소스/쇼핑아이콘.PNG')
    pil_image = pil_image.resize((90, 90), Image.ANTIALIAS)
    shopping_Button.image = ImageTk.PhotoImage(pil_image)
    shopping_Button = Button(image = shopping_Button.image, command=lambda: clickicon())
    shopping_Button.place(x=900,y=10)
    shopping_text = Label(window)
    shopping_text.place(x=905, y=110)
    shopping_Button.bind("<Enter>", lambda _: shopping_text.configure(text="방역물품 쇼핑"))
    shopping_Button.bind("<Leave>", lambda _: shopping_text.configure(text=""))

def telegramButton():
    telegram_Button =Button(window)
    pil_image = Image.open('리소스/텔레그렘아이콘.PNG')
    pil_image = pil_image.resize((90, 90), Image.ANTIALIAS)
    telegram_Button.image = ImageTk.PhotoImage(pil_image)
    telegram_Button = Button(image = telegram_Button.image, command=lambda: clickicon())
    telegram_Button.place(x=1000,y=10)
    telegram_text = Label(window)
    telegram_text.place(x=1010, y=110)
    telegram_Button.bind("<Enter>", lambda _: telegram_text.configure(text="텔레그렘 봇"))
    telegram_Button.bind("<Leave>", lambda _: telegram_text.configure(text=""))


homeButton()
maskButton()
shoppingButton()
titleImage()
telegramButton()
window.mainloop()



