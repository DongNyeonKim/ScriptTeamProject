import requests
from tqdm import tqdm
import pandas as pd
import folium
from folium.plugins import MarkerCluster, MiniMap
import webbrowser
import CoronaMaskList
import numpy as np

# color_dic = {'plenty': 'limegreen', 'some': 'yellow', 'few': 'orangered', 'empty': 'whitesmoke', 'no_data': 'black'}
color_dic = { 'plenty':'green', 'some':'blue', 'few':'orange', 'empty':'red', 'no_data':'black' }

remain_stat_kor = { 'plenty':'100개 이상', 'some':'30개이상 100개미만', "few":'2개이상 30개 미만', "empty":"1개 이하", "no_data":"정보 없음" }


def getMaskStoreInfo():
    url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/stores/json?page=1"
    req = requests.get(url)
    total_page = req.json()['totalPages']
    addrs = []
    codes = []
    latitudes = []
    longitudes = []
    names = []
    types = []
    for page_num in tqdm(range(1, total_page+1)):
        url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/stores/json?page=" + str(page_num)
        req = requests.get(url)
        json_data = req.json()
        store_infos = json_data['storeInfos']
        for info in store_infos:
            addrs.append(info['addr'])
            codes.append(info['code'])
            latitudes.append(info['lat'])
            longitudes.append(info['lng'])
            names.append(info['name'])
            types.append(info['type'])

    mask_store_info_df = pd.DataFrame({"addr":addrs, "code":codes, "latitude":latitudes, "longitude":longitudes, "name":names, "type":types})

    return mask_store_info_df


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


#sales_dict = getMaskStoreSalesInfo()

#두 파일 합치기
def mergeSalesInfobyStoreCode(sales_dict, my_info_df):
    store_codes = list(my_info_df['code'])

    created_ats = []
    remain_stats = []
    stock_ats = []
    for i in tqdm(range(len(store_codes))):
        try:
            store_sales_info = sales_dict[str(store_codes[i])]

            created_ats.append(store_sales_info['created_at'])
            remain_stats.append(store_sales_info['remain_stat'])
            stock_ats.append(store_sales_info['stock_at'])
        except:
            created_ats.append("no_data")
            remain_stats.append("no_data")
            stock_ats.append("no_data")
    my_info_df['created_at'] = created_ats
    my_info_df['remain_stat'] = remain_stats
    my_info_df['stock_at'] = stock_ats

    return my_info_df


def executeMaskMap():
    my_info_df = getMaskStoreInfo()
    data_for_draw = my_info_df.loc[:, ['name', 'latitude', 'longitude']]
    data_for_draw_except_nan = data_for_draw.dropna()

    sales_dict = getMaskStoreSalesInfo()

    my_store_and_sales_info_df = mergeSalesInfobyStoreCode(sales_dict, my_info_df)
    data_for_draw2 = my_store_and_sales_info_df.loc[:, ['name', 'latitude', 'longitude', 'remain_stat']]
    data_for_draw2_nan = data_for_draw2.dropna()

    # 판매 중지 데이터 없애기
    data_for_draw_except_nan2 = data_for_draw2_nan[data_for_draw2_nan['remain_stat'] != 'break']

    map_hs2 = folium.Map((37.3402849,126.7313189), zoom_start = 15)
    # minimap = plugins.Minimap()
    # map_hs2.add_child(minimap)

    mc2 = MarkerCluster()

    names = list(data_for_draw_except_nan2['name'])
    latitudes = list(data_for_draw_except_nan2['latitude'])
    longitudes = list(data_for_draw_except_nan2['longitude'])
    remain_stats = list(data_for_draw_except_nan2['remain_stat'])

    for i in tqdm(range(len(names))):
        mc2.add_child(folium.Marker(location = [latitudes[i], longitudes[i]], icon=folium.Icon(color=color_dic[remain_stats[i]]), tooltip=names[i], popup=names[i] + ' ' + remain_stat_kor[remain_stats[i]]))
        map_hs2.add_child(mc2)
    map_hs2.save("./mask_store_total.html")

def openTotalMap():
    webbrowser.open_new('mask_store_total.html')

def getNearMaskStoreInfo(address):
    url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json?address=" + requests.utils.unquote(address)

    req = requests.get(url)

    json_data = req.json()
    store_data = json_data['stores']

    addrs = []
    codes = []
    latitudes = []
    longitudes = []
    names = []
    types = []
    created_ats = []
    remain_stats = []
    stock_ats = []
    for i in tqdm(range(len(store_data))):
        addrs.append(store_data[i]['addr'])
        codes.append(store_data[i]['code'])
        latitudes.append(store_data[i]['lat'])
        longitudes.append(store_data[i]['lng'])
        names.append(store_data[i]['name'])
        types.append(store_data[i]['type'])
        try:
            created_ats.append(store_data[i]['created_at'])
        except:
            created_ats.append("no_data")
        try:
            remain_stats.append(store_data[i]['remain_stat'])
        except:
            remain_stats.append("no_data")
        try:
            stock_ats.append(store_data[i]['stock_at'])
        except: stock_ats.append("no_data")

    print(len(addrs), len(codes), len(latitudes), len(longitudes), len(names), len(types), len(created_ats), len(remain_stats), len(stock_ats))

    mask_store_info_df = pd.DataFrame({"addr":addrs, "code":codes, "latitude":latitudes, "longitude":longitudes, "name":names, "type":types, "created_at":created_ats, "remain_stat":remain_stats, "stock_at":stock_ats})

    return mask_store_info_df


def makeSearchMapData():
    mask_store_info = getNearMaskStoreInfo(CoronaMaskList.addr)
    data_for_draw3 = mask_store_info.loc[:, ['name', 'latitude', 'longitude', 'remain_stat']]
    data_for_draw_except_nan3 = data_for_draw3.dropna()
    data_for_draw_except_nan3 = data_for_draw_except_nan3[data_for_draw_except_nan3['remain_stat'] != 'break']
    x= data_for_draw_except_nan3.loc[[1],['latitude']].values
    y= data_for_draw_except_nan3.loc[[1],['longitude']].values

    map_hs3 = folium.Map((x,y), zoom_start=14)

    mc3 = MarkerCluster()
    names = list(data_for_draw_except_nan3['name'])
    latitudes = list(data_for_draw_except_nan3['latitude'])
    longitudes = list(data_for_draw_except_nan3['longitude'])
    remain_stats = list(data_for_draw_except_nan3['remain_stat'])

    for i in tqdm(range(len(names))):
        mc3.add_child(folium.Marker(location=[latitudes[i], longitudes[i]], icon=folium.Icon(color=color_dic[remain_stats[i]]), popup=names[i] + ' ' + remain_stat_kor[remain_stats[i]]))
        map_hs3.add_child(mc3)

    map_hs3.save("./mask_store4.html")
    webbrowser.open_new('mask_store4.html')

#executeMaskMap()