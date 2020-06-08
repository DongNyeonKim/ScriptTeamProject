# from matplotlib import pyplot as plt
# from matplotlib import animation
# import numpy as np
# import random
# import time
# #
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure
# import tkinter as Tk
#
# fig = plt.figure()     #figure(도표) 생성
#
#
#
# ax = plt.subplot(211, xlim=(0, 50), ylim=(0, 1024))
# ax_2 = plt.subplot(212, xlim=(0, 50), ylim=(0, 512))
#
#
# max_points = 50
# max_points_2 = 50
#
#
# line, = ax.plot(np.arange(max_points),
#                 np.ones(max_points, dtype=np.float)*np.nan, lw=1, c='blue',ms=1)
# line_2, = ax_2.plot(np.arange(max_points_2),
#                 np.ones(max_points, dtype=np.float)*np.nan, lw=1,ms=1)
#
#
# def init():
#     return line
# def init_2():
#     return line_2
#
#
# def animate(i):
#     y = random.randint(0,1024)
#     old_y = line.get_ydata()
#     new_y = np.r_[old_y[1:], y]
#     line.set_ydata(new_y)
#     print(new_y)
#     return line
#
# def animate_2(i):
#     y_2 = random.randint(0,512)
#     old_y_2 = line_2.get_ydata()
#     new_y_2 = np.r_[old_y_2[1:], y_2]
#     line_2.set_ydata(new_y_2)
#     print(new_y_2)
#     return line_2
#
#
#
#
# root = Tk.Tk() #추가
# label = Tk.Label(root,text="라벨").grid(column=0, row=0)#추가
# canvas = FigureCanvasTkAgg(fig, master=root) #
# canvas.get_tk_widget().grid(column=0,row=1) #
#
#
#
# #anim = animation.FuncAnimation(fig, animate  , init_func= init ,frames=200, interval=50, blit=False)
# #anim_2 = animation.FuncAnimation(fig, animate_2  , init_func= init_2 ,frames=200, interval=10, blit=False)
# Tk.mainloop()


import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import HomeUI


data2 = {'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
         'Unemployment_Rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
         }
df2 = DataFrame(data2, columns=['Year', 'Unemployment_Rate'])




def makegrape(window):
    figure2 = plt.Figure(figsize=(4, 4), dpi=80)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, window)
    line2.get_tk_widget().place(x=600, y=150)
    df21 = df2[['Year', 'Unemployment_Rate']].groupby('Year').sum()
    df21.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
    ax2.set_title('Year Vs. Unemployment Rate')


