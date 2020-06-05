# from tkinter import *
# from PIL import Image, ImageTk
#
#
# def titleImage():
#     title_label = Label()
#     title_label.image = PhotoImage(file = "리소스/코로나종합상황센터.PNG")
#     title_label['image'] = title_label.image
#     title_label.place(x=20,y=10)
#
# def clickicon():
#     print("Click")
#
#
# def homeButton():
#     home_Button =Button()
#     pil_image = Image.open('리소스/홈버튼.JPG')
#     pil_image = pil_image.resize((90, 90), Image.ANTIALIAS)
#     home_Button.image = ImageTk.PhotoImage(pil_image)
#     home_Button = Button(image = home_Button.image, command=lambda: clickicon())
#     home_Button.place(x=700,y=10)
#     home_text = Label()
#     home_text.place(x=735, y=110)
#     home_text.configure(background='LightSteelBlue1')
#     home_Button.bind("<Enter>", lambda _: home_text.configure(text="홈"))
#     home_Button.bind("<Leave>", lambda _: home_text.configure(text=""))
#
#
#
# def shoppingButton():
#     shopping_Button =Button()
#     pil_image = Image.open('리소스/쇼핑아이콘.PNG')
#     pil_image = pil_image.resize((90, 90), Image.ANTIALIAS)
#     shopping_Button.image = ImageTk.PhotoImage(pil_image)
#     shopping_Button = Button(image = shopping_Button.image, command=lambda: clickicon())
#     shopping_Button.place(x=900,y=10)
#     shopping_text = Label()
#     shopping_text.place(x=905, y=110)
#     shopping_text.configure(background='LightSteelBlue1')
#     shopping_Button.bind("<Enter>", lambda _: shopping_text.configure(text="방역물품 쇼핑"))
#     shopping_Button.bind("<Leave>", lambda _: shopping_text.configure(text=""))
#
# def telegramButton():
#     telegram_Button =Button()
#     pil_image = Image.open('리소스/텔레그렘아이콘.PNG')
#     pil_image = pil_image.resize((90, 90), Image.ANTIALIAS)
#     telegram_Button.image = ImageTk.PhotoImage(pil_image)
#     telegram_Button = Button(image = telegram_Button.image, command=lambda: clickicon())
#     telegram_Button.place(x=1000,y=10)
#     telegram_text = Label()
#     telegram_text.place(x=1010, y=110)
#     telegram_text.configure(background='LightSteelBlue1')
#     telegram_Button.bind("<Enter>", lambda _: telegram_text.configure(text="텔레그렘 봇"))
#     telegram_Button.bind("<Leave>", lambda _: telegram_text.configure(text=""))
#
#
# def search():
#     print("search")
#
#
# def searchcoronanewsButton():
#     coronanews_Button = Button(command = search)
#     coronanews_Button.place(x=60,y=500)
#     coronanews_Button.configure(text= "  코로나 관련 \n 뉴스기사 검색", font = ('서울서체',20,'bold'),
#                                 height = 2, width=12,
#                                 background='SteelBlue1')
#
# def searchScreeningClinicButton():
#     coronanews_Button = Button()
#     coronanews_Button.place(x=320,y=500)
#     coronanews_Button.configure(text= "선별진료소 검색", font = ('서울서체',20,'bold'),
#                                 height = 2, width=12,
#                                 background='SteelBlue1')
# def searchScreeningCarClinicButton():
#     coronanews_Button = Button()
#     coronanews_Button.place(x=570,y=500)
#     coronanews_Button.configure(text= "  승차검진 \n진료소 검색", font = ('서울서체',20,'bold'),
#                                 height = 2, width=12,
#                                 background='SteelBlue1')
# def searchSafetyHospitalButton():
#     coronanews_Button = Button()
#     coronanews_Button.place(x=820,y=500)
#     coronanews_Button.configure(text= "안심병원 검색", font = ('서울서체',20,'bold'),
#                                 height = 2, width=12,
#                                 background='SteelBlue1')
#
# class SampleApp(Tk):
#     def __init__(self):
#         Tk.__init__(self)
#         self._frame = None
#         self.switch_frame(StartPage)
#         self.title("Covid-19 ControlCenter")
#         self.geometry("1100x600")
#         self.configure(background='LightSteelBlue1')
#         self.resizable(0,0)
#
#     def switch_frame(self, frame_class):
#         new_frame = frame_class(self)
#         if self._frame is not None:
#             self._frame.destroy()
#         self._frame = new_frame
#         self._frame.pack()
#
# class StartPage(Frame):
#     def __init__(self, master):
#         Frame.__init__(self, master)
#         homeButton()
#         self.maskButton(master)
#         shoppingButton()
#         titleImage()
#         telegramButton()
#         searchcoronanewsButton()
#         searchScreeningClinicButton()
#         searchScreeningCarClinicButton()
#         searchSafetyHospitalButton()
#         Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)
#         Button(self, text="Open page one",
#                   command=lambda: master.switch_frame(PageOne)).pack()
#         Button(self, text="Open page two",
#                   command=lambda: master.switch_frame(PageTwo)).pack()
#
#     def maskButton(self, master):
#         self.mask_Button = Button()
#         pil_image = Image.open('리소스/마스크아이콘.PNG')
#         pil_image = pil_image.resize((90, 90), Image.ANTIALIAS)
#         self.mask_Button.image = ImageTk.PhotoImage(pil_image)
#         self.mask_Button = Button(image=self.mask_Button.image, command=lambda: master.switch_frame(PageOne))
#         self.mask_Button.place(x=800, y=10)
#         self.mask_text = Label()
#         self.mask_text.place(x=800, y=110)
#         self.mask_text.configure(background='LightSteelBlue1')
#         self.mask_Button.bind("<Enter>", lambda _: self.mask_text.configure(text="공적마스크 검색"))
#         self.mask_Button.bind("<Leave>", lambda _: self.mask_text.configure(text=""))
#
#
# class PageOne(Frame):
#     def __init__(self, master):
#         Frame.__init__(self, master)
#         Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
#         Button(self, text="Return to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()
#
# class PageTwo(Frame):
#     def __init__(self, master):
#         Frame.__init__(self, master)
#         Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
#         Button(self, text="Return to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()
#
# if "__main__":
#     app = SampleApp()
#     app.mainloop()
#
#
#
#
from tkinter import *


def raise_frame(frame):
    frame.tkraise()

root = Tk()

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')

Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
Label(f1, text='FRAME 1').pack()

Label(f2, text='FRAME 2').pack()
Button(f2, text='Go to frame 3', command=lambda:raise_frame(f3)).pack()

Label(f3, text='FRAME 3').pack(side='left')
Button(f3, text='Go to frame 4', command=lambda:raise_frame(f4)).pack(side='left')

Label(f4, text='FRAME 4').pack()
Button(f4, text='Goto to frame 1', command=lambda:raise_frame(f1)).pack()

raise_frame(f1)
root.mainloop()