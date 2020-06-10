from tkinter import *
from PIL import Image, ImageTk
import PIL.ImageTk

from tkinter import font
import tkinter.messagebox
import tkinter.ttk
import MaskUI
import ShoppingUI
import SearchFunction
import CoronaStateXMLParsing as CS
import CoronaGraph

def MoveMaskState():
    window.destroy()
    MaskUI.MaskState()

def MoveShoppingState():
    window.destroy()
    ShoppingUI.ShoppingState()

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
    home_Button = Button(image = home_Button.image)
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
    mask_Button = Button(image = mask_Button.image, command=lambda: MoveMaskState())
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
    telegram_Button = Button(image = telegram_Button.image, command=lambda: clickicon())
    telegram_Button.place(x=1000,y=10)
    telegram_text = Label(window)
    telegram_text.place(x=1010, y=110)
    telegram_text.configure(background='LightSteelBlue1')
    telegram_Button.bind("<Enter>", lambda _: telegram_text.configure(text="텔레그렘 봇"))
    telegram_Button.bind("<Leave>", lambda _: telegram_text.configure(text=""))


def search():
    print("search")


def searchcoronanewsButton():
    coronanews_Button = Button(window, command=lambda: SearchFunction.getCoronanews())
    coronanews_Button.place(x=60,y=500)
    coronanews_Button.configure(text= "  코로나 관련 \n 뉴스기사 검색", font = ('서울서체',20,'bold'),
                                height = 2, width=12,
                                background='SteelBlue1')

def searchScreeningClinicButton():
    coronanews_Button = Button(window, command=lambda: SearchFunction.getScreeningClinic())
    coronanews_Button.place(x=320,y=500)
    coronanews_Button.configure(text= "선별진료소 검색", font = ('서울서체',20,'bold'),
                                height = 2, width=12,
                                background='SteelBlue1')
def searchScreeningCarClinicButton():
    coronanews_Button = Button(window, command=lambda: SearchFunction.getScreeningCarClinic())
    coronanews_Button.place(x=570,y=500)
    coronanews_Button.configure(text= "  승차검진 \n진료소 검색", font = ('서울서체',20,'bold'),
                                height = 2, width=12,
                                background='SteelBlue1')
def searchSafetyHospitalButton():
    coronanews_Button = Button(window, command=lambda: SearchFunction.getSafetyHospital())
    coronanews_Button.place(x=820,y=500)
    coronanews_Button.configure(text= "안심병원 검색", font = ('서울서체',20,'bold'),
                                height = 2, width=12,
                                background='SteelBlue1')

def CoronaStatus():
    date_label = Label(window)
    date_label.place(x=20, y=150)
    date_label.configure(text="날짜", font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='lightgray', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=20, y=186)
    date_label.configure(text="확진자", font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='lightgray', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=20, y=222)
    date_label.configure(text="사망자", font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='lightgray', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=20, y=258)
    date_label.configure(text="치료중", font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='lightgray', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=20, y=294)
    date_label.configure(text="검사진행", font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='lightgray', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=20, y=330)
    date_label.configure(text="완치자", font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='lightgray', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=20, y=366)
    date_label.configure(text="음성결과", font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='lightgray', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=20, y=402)
    date_label.configure(text="누적검사완료", font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='lightgray', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=20, y=438)
    date_label.configure(text="누적검사", font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='lightgray', relief = 'groove')

    date_label = Label(window)
    date_label.place(x=195, y=114)
    date_label.configure(text="금일", font=('Arial', 20, 'bold'),
                         height=1, width=10,
                         background='gray', relief='groove')
    date_label = Label(window)
    date_label.place(x=370, y=114)
    date_label.configure(text="전일", font=('Arial', 20, 'bold'),
                         height=1, width=10,
                         background='gray', relief='groove')

    date_label = Label(window, width= 60)
    date_label.place(x=195, y=150)
    date_label.configure(text=CS.data[0]['date'], font=('Arial', 20,'bold'),
                                height=1, width=10,
                                background='white', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=195, y=186)
    date_label.configure(text=CS.data[0]['getCorona'], font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='white', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=195, y=222)
    date_label.configure(text=CS.data[0]['death'], font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='white', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=195, y=258)
    date_label.configure(text=CS.data[0]['care'], font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='white', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=195, y=294)
    date_label.configure(text=CS.data[0]['exam'], font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='white', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=195, y=330)
    date_label.configure(text=CS.data[0]['clear'], font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='white', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=195, y=366)
    date_label.configure(text=CS.data[0]['resutlNeg'], font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='white', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=195, y=402)
    date_label.configure(text=CS.data[0]['doneExam'], font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='white', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=195, y=438)
    date_label.configure(text=CS.data[0]['totalExam'], font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='white', relief = 'groove')

    date_label = Label(window, width= 60)
    date_label.place(x=370, y=150)
    date_label.configure(text=CS.data[1]['date'], font=('Arial', 20,'bold'),
                                height=1, width=10,
                                background='white', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=370, y=186)
    date_label.configure(text=CS.data[1]['getCorona'], font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='white', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=370, y=222)
    date_label.configure(text=CS.data[1]['death'], font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='white', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=370, y=258)
    date_label.configure(text=CS.data[1]['care'], font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='white', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=370, y=294)
    date_label.configure(text=CS.data[1]['exam'], font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='white', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=370, y=330)
    date_label.configure(text=CS.data[1]['clear'], font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='white', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=370, y=366)
    date_label.configure(text=CS.data[1]['resutlNeg'], font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='white', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=370, y=402)
    date_label.configure(text=CS.data[1]['doneExam'], font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='white', relief = 'groove')
    date_label = Label(window)
    date_label.place(x=370, y=438)
    date_label.configure(text=CS.data[1]['totalExam'], font=('Arial', 20, 'bold'),
                                height=1, width=10,
                                background='white', relief = 'groove')
    text_label = Label(window)
    text_label.place(x=150, y=475)
    text_label.configure(text="※금일 데이터가 업데이트 안되었을 경우 전일 데이터를 불러옵니다.",
                         background='LightSteelBlue1', font=('Arial', 10))


def HomeState():
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
    searchcoronanewsButton()
    searchScreeningClinicButton()
    searchScreeningCarClinicButton()
    searchSafetyHospitalButton()

    CoronaStatus()
    CoronaGraph.makegrape(window)
    window.mainloop()





