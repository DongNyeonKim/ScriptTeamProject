from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
import tkinter.messagebox
import HomeUI
import MaskUI
import ShoppingList
import CrowlingShoppingList as CSL
import urllib.request
from io import BytesIO
import EmailSending as ES

def MoveHomeState():
    window.destroy()
    HomeUI.HomeState()

def MoveMaskState():
    window.destroy()
    MaskUI.MaskState()

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
    mask_Button = Button(image = mask_Button.image,command=lambda: MoveMaskState())
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
    shopping_Button = Button(image = shopping_Button.image)
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

def titlelabel():
    title = Label(window,text ="방역물품 \n쇼핑", font=('서울서체', 25, 'bold'),fg = "midnightblue", bg = 'cornflowerblue', width = 12, height = 6)
    title.place(x=100,y=150)

def infolabel():
    info = Label(window,text ="검색할 물품을 선택하시고 검색버튼을 누르시오.", font=('서울서체', 15, 'bold'),bg = "LightSteelBlue1")
    info.place(x=580,y=400)

def excelsavebutton():
    excelsave_Button =Button(window)
    pil_image = Image.open('리소스/엑셀아이콘.PNG')
    pil_image = pil_image.resize((90, 90), Image.ANTIALIAS)
    excelsave_Button.image = ImageTk.PhotoImage(pil_image)
    excelsave_Button = Button(image = excelsave_Button.image, bg ='snow', command=lambda: CSL.excelsavefile(CSL.search))
    excelsave_Button.place(x=100,y=420)
    excel_text = Label(window, text="전체검색항목\n엑셀 저장")
    excel_text.place(x=85, y=530)
    excel_text.configure(background='LightSteelBlue1', font=('서울서체', 15, 'bold'))

def imagesavebutton():
    imagesave_Button =Button(window)
    pil_image = Image.open('리소스/사진.png')
    pil_image = pil_image.resize((90, 90), Image.ANTIALIAS)
    imagesave_Button.image = ImageTk.PhotoImage(pil_image)
    imagesave_Button = Button(image = imagesave_Button.image, bg ='snow', command=lambda: CSL.imagesavefile(CSL.search))
    imagesave_Button.place(x=260,y=420)
    image_text = Label(window, text="전체검색항목\n이미지 저장")
    image_text.place(x=240, y=530)
    image_text.configure(background='LightSteelBlue1', font=('서울서체', 15, 'bold'))

def emailsendingbutton():
    emailsending_Button =Button(window)
    pil_image = Image.open('리소스/이메일아이콘.png')
    pil_image = pil_image.resize((60, 60), Image.ANTIALIAS)
    emailsending_Button.image = ImageTk.PhotoImage(pil_image)
    emailsending_Button = Button(image = emailsending_Button.image, bg ='snow', command=lambda: ES.writeyourEmail())
    emailsending_Button.place(x=1000,y=520)
    # image_text = Label(window, text="전체검색항목\n이미지 저장")
    # image_text.place(x=240, y=530)
    # image_text.configure(background='LightSteelBlue1', font=('서울서체', 15, 'bold'))

def searchRadiobutton():
    global var
    var = IntVar()
    mask = Radiobutton(window, text = "마스크", value = 1, variable=var, font=('서울서체', 15, 'bold'), background ="LightSteelBlue1", command =radiobuttonCommand)
    mask.place(x=550,y=150)
    hand = Radiobutton(window, text = "손소독제", value = 2,variable=var, font=('서울서체', 15, 'bold'),background ="LightSteelBlue1",command =radiobuttonCommand)
    hand.place(x=700,y=150)
    heat = Radiobutton(window, text = "체온계", value = 3,variable=var, font=('서울서체', 15, 'bold'),background ="LightSteelBlue1",command =radiobuttonCommand)
    heat.place(x=850,y=150)
    heat = Radiobutton(window, text = "기타", value = 4,variable=var, font=('서울서체', 15, 'bold'), background ="LightSteelBlue1",command =radiobuttonCommand)
    heat.place(x=550,y=200)

    global searchitem
    searchitem = "이외 검색할 물품을 입력하시오."
    global iptsearchitem
    iptsearchitem = Entry(window, state = 'disabled')  # 주소 입력받는 인풋 위젯
    iptsearchitem.insert(0, searchitem)
    iptsearchitem.place(x=650, y=200, height=30)
    iptsearchitem.configure(width=25, background='white', font=('서울서체', 15, 'bold'))

    btnSearch = Button(window, text="검색", width=14, command = searchButtonCommand)
    btnSearch.place(x=950, y=200, height=30)
    btnSearch.configure(background='white', font=('서울서체', 10, 'bold'))

def radiobuttonCommand():
    a = var.get()
    if a ==1:
        CSL.search = "마스크"
        iptsearchitem.configure(state='disabled')
    if a ==2:
        CSL.search = "손소독제"
        iptsearchitem.configure(state='disabled')
    if a ==3:
        CSL.search = "체온계"
        iptsearchitem.configure(state='disabled')
    if a ==4:
        iptsearchitem.configure(state='normal')


def searchButtonCommand():
    if  var.get() ==4:
        CSL.search = iptsearchitem.get()
    CSL.crowlingShoppingList()
    ShoppingList.makeShoppingList(window)

def ShoppingState():
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
    searchRadiobutton()

    titlelabel()
    infolabel()
    excelsavebutton()
    imagesavebutton()
    emailsendingbutton()

    window.mainloop()







