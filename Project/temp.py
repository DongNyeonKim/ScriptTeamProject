import requests
import json
from tqdm import tqdm
import requests as rq
import json
import tkinter as tk
import tkinter.ttk as ttk
import webbrowser as wbs
import tkinter.messagebox as tkMsg

def getMaskStoreSalesInfo():
    url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/sales/json?page=1"
    req = requests.get(url)
    total_page = req.json()['totalPages']
    sales_dict = {}
    for page_num in tqdm(range(1, total_page+1)):
        url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/sales/json?page=" + str(page_num)
        req = requests.get(url)
        json_data = req.json()
        sales_infos = json_data['sales']
        print(sales_infos)
        for i in range(len(sales_infos)):
            code = sales_infos[i]['code']
            try:
                created_at = sales_infos[i]['created_at']
            except:
                created_at = "no_data"
            try:
                remain_stat = sales_infos[i]['remain_stat']
            except:
                remain_stat = "no_data"
            try:
                stock_at = sales_infos[i]['stock_at']
            except:
                stock_at = "no_data"

            sales_dict[code] = {"created_at":created_at, "remain_stat":remain_stat, "stock_at":stock_at}

    return sales_dict

header = ["판매처","주소","재고량","입고일시","생성일시"]
stores = getMaskStoreSalesInfo()

#해당 주소로 판매처 및 재고현황 정보 요청
def requetJson():
    pass #3.2에서 코딩
