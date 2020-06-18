from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import CoronaStateXMLParsing as CS

#한글 폰트 적용
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


data2 = {'날짜': [ CS.data[0]['date'], CS.data[1]['date'],  CS.data[2]['date'],  CS.data[3]['date'],  CS.data[4]['date'],  CS.data[5]['date'],  CS.data[6]['date']],
         '일확진자': [int(CS.data[0]['getCorona'])-int(CS.data[1]['getCorona']), int(CS.data[1]['getCorona'])-int(CS.data[2]['getCorona']), int(CS.data[2]['getCorona'])-int(CS.data[3]['getCorona']),
                              int(CS.data[3]['getCorona'])-int(CS.data[4]['getCorona']), int(CS.data[4]['getCorona'])-int(CS.data[5]['getCorona']), int(CS.data[5]['getCorona'])-int(CS.data[6]['getCorona']),
                              int(CS.data[6]['getCorona'])-int(CS.data[7]['getCorona'])]
         }
df2 = DataFrame(data2, columns=['날짜', '일확진자'])

df2=df2.astype({'일확진자':int})


def makegrape(window):
    figure2 = plt.Figure(figsize=(6, 4), dpi=80)
    ax2 = figure2.add_subplot(111)
    list = [i for i in range(0,100,2)]
    ax2.set_yticks(list)
    line2 = FigureCanvasTkAgg(figure2, window)
    line2.get_tk_widget().place(x=600, y=150)
    df21 = df2[["날짜", "일확진자"]].groupby("날짜").sum()
    df21.plot(kind='line', legend=True, ax=ax2, color='r', marker='o',fontsize=10)

    l_getco = data2["일확진자"]
    for i in (range(7)):
        ax2.scatter(6-i, l_getco[i])
        ax2.text(6-i+0.2,l_getco[i],  "{}".format(l_getco[i]), fontsize=15)

    ax2.set_yticklabels(list, fontsize=15)
    ax2.set_xlabel("날짜",fontsize=12,weight='bold')
    ax2.set_ylabel("일확진자",fontsize=12,weight='bold')
    ax2.set_title("최근 7일 일일확진자",fontsize=20,weight='bold')