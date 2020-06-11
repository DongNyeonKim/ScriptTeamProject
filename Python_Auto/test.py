from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import urllib
import urllib.request

newImg = None
newImg2 = None

def evInser():

    url = "https://search.pstatic.net/common/?src=https%3A%2F%2Fsearchad-phinf.pstatic.net%2FMjAyMDA2MDhfODUg%2FMDAxNTkxNTk3ODQ0MzU1.fFBqn_5f_l0qtrQYeH44EMSoR8Zn7Ed1Fz7N_WYGU7Ig.lHuXhI75h51qMIzizKJ1w7Dnvf71yG3J44o9VjTsYsog.JPEG%2F30949-94de08fa-9d16-4896-80eb-4b3486c8931f.jpg&amp;type=w&amp;size=200"
    with urllib.request.urlopen(url) as u:
        global newImg2
        raw_data = u.read()
        im = Image.open(BytesIO(raw_data))
        newImg2 = ImageTk.PhotoImage(im)
        #canvas2.create_image(105, 39, image = newImg2)
        label2.configure(image=newImg2)

top = Tk()



label2 = Label(top,text="url file load")
label2.pack()

A = Button(top, text="로컬과 웹의 이미지로드 버튼", command=evInser)
A.pack()
top.mainloop()