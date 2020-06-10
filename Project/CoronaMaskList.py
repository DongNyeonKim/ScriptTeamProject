import requests as rq
import json
from tkinter import *
import tkinter.ttk as ttk
import webbrowser as wbs
import tkinter.messagebox as tkMsg
import MaskUI


#해당 주소로 판매처 및 재고현황 정보 요청
def requetJson():
    global addr
    # 응답코드(status_code) 반환
    # 200: 성공, 404:  존재하지 않는 URL
    addr = iptAddr.get()
    res = rq.get(url, params={"address": addr})  # rq.post()
    print(res.status_code)
    if res.status_code == 200:
        print("[요청성공]")
    else:
        print("[알수 없는 에러:%s]\n " % res)
        return -1

    # load json data
    return json.loads(res.content)

def fixed_map(option):
    return [elm for elm in style.map('Treeview', query_opt=option) if
      elm[:2] != ('!disabled', '!selected')]

#해당 주소로 판매처 및 재고현황 정보 가져와서 표시
def infoSearch():
    # 기존 데이터 있다면 삭제
    for row in trv.get_children():
        trv.delete(row)

    global stores
    jData = requetJson()
    # 데이터를 제대로 받아오지 못했다면 메세지창으로 알림
    if type(jData) == int:
        tkMsg.showerror("실패", "요청을 실패하였습니다.")
        return -1
    # print(type(jData)) # dict
    # print info(stores)
    cnt = 0
    for store in jData['stores']:
        # remain_stat : None, empty, few, some, plenty
        # empty : 회색(0~1개)/
        # few: 빨강색(2~29개)/some: 노랑색(30~99개)/ plenty: 녹색(100개 이상)
        status = store.get('remain_stat')
        if status in ["few", "some", "plenty","empty","black"]:
            # header = ["판매처","주소","재고량","입고일시","생성일시"]
            info = (store.get('name'),
                    store.get('addr').replace(iptAddr.get(), "")
                    , status, store.get('stock_at')
                    , store.get('created_at'))
            stores.append(info)
            cnt += 1
            # 재고 상태에 따라 색상 변경 해줄려고 재고 상태를 태그로 달아줌
            trv.insert('', 'end', text=cnt, values=info, tags=[status])
            #print(stores) #추출한 데이터 확인
    # 재고 상태별 행 색상 변경(적용이 안된다면 3.3 버그 해결부분 참고)
    trv.tag_configure('plenty', background="limegreen")
    trv.tag_configure('some', background="yellow")
    trv.tag_configure('few', background="orangered")
    trv.tag_configure('empty', background="whitesmoke")
    trv.tag_configure('black', background="black")

'''
 더블클릭시 해당 판매처 위치 검색(네이버)
'''
def OnDoubleClick(e):
#treeview에서 선택된 아이템정보 가져오기
  selectedItem = trv.item(trv.selection()[0])['values']
  # 0: name, 1: addr, 2: remain (주소와 판매처 이름 합치기)
  selectedAddr = iptAddr.get()+selectedItem[1]
 # print(selectedAddr) #합친 주소정보 확인
  naverURL = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query="
  param = selectedAddr+" "+selectedItem[0]
  print(param) # 보낼 데이터 확인
  wbs.open(naverURL+param, new=1) #해당 주소로 인터넷창 팝업



def makeMaskList(window):
    global url
    url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json"
    global addr
    addr = "경기도 시흥시"  # default address
    global header
    header = ["판매처", "주소", "재고량", "입고일시", "생성일시"]
    global stores
    stores = []  # store list
    #타이틀
    title = Label(window)
    title.place(x=200, y=110)
    title.configure(text= "공적마스크 판매처 검색", font = ('서울서체',20,'bold'),
                                height = 2, width=20,
                                background='LightSteelBlue1')
    # 입력받는 곳
    lb1 = Label(window)
    lb1.place(x=100, y=180)
    lb1.configure(text="주소 : ", font = ('서울서체',15,'bold'),
                                background='LightSteelBlue1')

    global iptAddr
    iptAddr = Entry(window)  # 주소 입력받는 인풋 위젯
    iptAddr.insert(0, addr)
    iptAddr.place(x=160, y=180,height=30)
    iptAddr.configure(width = 25, background='white',font = ('서울서체',15,'bold'))

    btnSearch = Button(window, text="Search", width=15, command=infoSearch)
    btnSearch.place(x=440, y=180,height=30)
    btnSearch.configure(background='white',font = ('서울서체',10,'bold'))
    # 안내 문구
    lb2_plenty = Label(window, text="plenty(Green) - 100개 이상")
    lb2_plenty.place(x=590, y=115)
    lb2_plenty.configure(foreground = 'green', background='LightSteelBlue1', font=('서울서체', 8, 'bold'))

    lb2_some = Label(window, text="some(Yellow) - 30~99개")
    lb2_some.place(x=590, y=135)
    lb2_some.configure(foreground = 'yellow', background='LightSteelBlue1', font=('서울서체', 8, 'bold'))

    lb2_few = Label(window, text="few(Red) - 2~29개")
    lb2_few.place(x=590, y=155)
    lb2_few.configure(foreground = 'red', background='LightSteelBlue1', font=('서울서체', 8, 'bold'))


    lb2_empty = Label(window, text="empty(White) - 1개 이하")
    lb2_empty.place(x=590, y=175)
    lb2_empty.configure(foreground = 'white', background='LightSteelBlue1', font=('서울서체', 8, 'bold'))

    lb2_black = Label(window, text="black(Black) - 판매중지")
    lb2_black.place(x=590, y=195)
    lb2_black.configure(foreground = 'black', background='LightSteelBlue1', font=('서울서체', 8, 'bold'))

    lb2 = Label(window)
    lb2.place(x=60, y=560)
    lb2.configure(text="※데이터 더블클릭 시 위치 검색", font=("",10, 'bold'),
              background='LightSteelBlue1')
    lb3 = Label(window)
    lb3.place(x=300, y=560)
    lb3.configure(text="※주소 입력 예시 >서울특별시 양천구, 강원도 춘천시[시, 구 까지 입력]", font=("",10, 'bold'),
              background='LightSteelBlue1')
    # 판매현황표시 --> treeview(like table)
    global trv
    trv = ttk.Treeview(window, columns=header, displaycolumns=header, padding=5)
    ttk.Style().configure('Treeview', rowheight=30)
    # 트리뷰 스크롤 추가
    scrY = ttk.Scrollbar(orient='vertical', command=trv.yview)
    scrY.place(x=724, y=220,height=335)
    trv.config(yscrollcommand=scrY.set)
    trv.place(x=60, y=220)
    trv.columnconfigure(0, weight=1)

    # 데이터 header 설정
    trv.column('#0', width=40, anchor="center")
    trv.heading("#0", text="No.", anchor="center")
    trv.column('#1', width=100)  # store name
    trv.heading("#1", text=header[0], anchor="center")
    trv.column('#2')  # addr
    trv.heading('#2', text=header[1], anchor="center")
    trv.column('#3', width=50)  # remain_stat
    trv.heading('#3', text=header[2], anchor="center")
    trv.column('#4', width=130)  # stock_at
    trv.heading('#4', text=header[3], anchor="center")
    trv.column('#5', width=130)  # created_at
    trv.heading('#5', text=header[4], anchor="center")
    global style
    style = ttk.Style()
    style.map('Treeview', foreground=fixed_map('foreground'),
              background=fixed_map('background'))

    trv.bind("<Double-1>", OnDoubleClick)