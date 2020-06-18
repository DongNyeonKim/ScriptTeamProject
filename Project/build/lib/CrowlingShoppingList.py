import csv
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import os
import ShoppingUI

def crowlingShoppingList():
    global search
    url = f'https://msearch.shopping.naver.com/search/all?query={quote_plus(search)}'
    html = urlopen(url).read()
    global soup
    soup = BeautifulSoup(html,'html.parser')
    total = soup.select('._2TFfLkGZhc')
    global SearchList
    SearchList = []
    num=1
    for i in total:
        temp = []
        tagname = search+str(num)
        names = i.select('._3ldP-RMmbZ')
        name = names[0].text
        prices = i.select('._1vPmSw6Psr')
        price = prices[0].find("strong").text + '원'
        url = soup.select('._1SwezRSbBH > a')[0]['href']

        urls = i.select('._2oDyaXK-qb')[0]
        siteURL = urls.get('href')
        if siteURL == None:
            siteURL = i.get('href')

        imageurls = i.select('._2oDyaXK-qb > img')[0]
        imgaeURL = imageurls.get('src')

        num += 1
        temp.append(tagname)
        temp.append(name)
        temp.append(price)
        temp.append(siteURL)
        temp.append(imgaeURL)
        SearchList.append(temp)



#액셀 저장
def excelsavefile(search):
    try:
        if not os.path.exists("쇼핑리스트저장파일"):
            os.makedirs("쇼핑리스트저장파일")
    except:
        pass
    f = open(f'쇼핑리스트저장파일/{search}쇼핑리스트.csv','w', newline='')
    csvWriter = csv.writer(f)
    for i in SearchList:
        csvWriter.writerow(i)
    f.close()

    print("Excel_Save_Done!!")
    #

#이미지 저장
def imagesavefile(filename):
    foldername = f'{filename}이미지저장파일'
    try:
        if not os.path.exists(foldername):
            os.makedirs(foldername)
    except:
        pass
    images = soup.select('._2oDyaXK-qb > img')
    n=1
    for i in images:
        imgURL = i.attrs['src']
        with urlopen(imgURL) as f:
            with open(foldername+"/"+search + str(n)+ '.jpg', 'wb') as h:
                img = f.read()
                h.write(img)
        n += 1
    print('ImageDown_Done!!')