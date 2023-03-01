'''show_pic.py'''
from  tkinter import *
import random
from PIL import Image, ImageTk
import glob
from PIL import Image
import tkinter.messagebox
import cv2
import numpy as np

    
class Apps:
    def __init__(self):
        self.windows = Toplevel() #子界面必须是Toplevel，否则无法显示图片
        self.windows.title("身材相册")
        self.windows.geometry('+%d+%d' % (0, 0))  #只设置了子界面的位置，没有设置大小，会随照片而变化
        self.count=0
        self.creat_res()
        self.windows.mainloop()

    #初始化子界面组件并显示第一张图片  
    def creat_res(self):
        self.temp=StringVar()
        picp = glob.glob("res/pic/*.*")  #照片路径
        pic=picp[self.count]
        load = Image.open(pic)
        #为了获取照片的长和宽，用opencv重新读取了一下，Image.open打开的图片貌似没有这两个属性
        img=cv2.imdecode(np.fromfile(pic,dtype=np.uint8),-1)  #如果有中文名称，不能直接用cv2.imread
        #根据图片大小进行放大和缩小，以实现较好的视觉效果
        if 200<img.shape[1]<500 and 200<img.shape[0]<500:
            pass
        elif img.shape[1]<200 and img.shape[0]<200:
            load = load.resize((int(img.shape[1]*3), int(img.shape[0]*3)),Image.ANTIALIAS)
        else:
            load = load.resize((int(img.shape[1]/2), int(img.shape[0]/2)),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        #初始化label的图片为相册第一张
        self.L2=Label(self.windows,image=render)
        self.L2.grid(sticky='nw')
        #绑定鼠标事件进行翻页
        self.L2.bind('<Button-3>', self.next)  #右键下一张
        self.L2.bind('<Button-1>', self.pre)  #左键上一张
        self.windows.mainloop()

    #下一张
    def next(self,aa):
        self.count+=1  #用来给照片计数，到达最后一张照片后清零，从头播放
        try:
            picp = glob.glob("res/pic/*.*")
            pic=picp[self.count] 	
            load = Image.open(pic)
            img=cv2.imdecode(np.fromfile(pic,dtype=np.uint8),-1)      
            if 200<img.shape[1]<500 and 200<img.shape[0]<500:
                pass
            elif img.shape[1]<200 and img.shape[0]<200:
                load = load.resize((int(img.shape[1]*3), int(img.shape[0]*3)),Image.ANTIALIAS)
            else:
                load = load.resize((int(img.shape[1]/2), int(img.shape[0]/2)),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)	
            self.L2.config(image=render)
            self.windows.mainloop()
        except:
            self.count=0
            picp = glob.glob("res/pic/*.*")
            pic=picp[self.count] 	
            load = Image.open(pic)
            img=cv2.imdecode(np.fromfile(pic,dtype=np.uint8),-1)       
            if 200<img.shape[1]<500 and 200<img.shape[0]<500:
                pass
            elif img.shape[1]<200 and img.shape[0]<200:
                load = load.resize((int(img.shape[1]*3), int(img.shape[0]*3)),Image.ANTIALIAS)
            else:
                load = load.resize((int(img.shape[1]/2), int(img.shape[0]/2)),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)	
            self.L2.config(image=render)
            self.windows.mainloop()	
    #上一张
    def pre(self,aa):
        self.count-=1  
        try:
            picp = glob.glob("res/pic/*.*")
            pic=picp[self.count] 	
            load = Image.open(pic)
            img=cv2.imdecode(np.fromfile(pic,dtype=np.uint8),-1)      
            if 200<img.shape[1]<500 and 200<img.shape[0]<500:
                pass
            elif img.shape[1]<200 and img.shape[0]<200:
                load = load.resize((int(img.shape[1]*3), int(img.shape[0]*3)),Image.ANTIALIAS)
            else:
                load = load.resize((int(img.shape[1]/2), int(img.shape[0]/2)),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)	
            self.L2.config(image=render)
            self.windows.mainloop()
        except:
            picp = glob.glob("res/pic/*.*")
            self.count=len(picp)-1
            pic=picp[self.count] 	
            load = Image.open(pic)
            img=cv2.imdecode(np.fromfile(pic,dtype=np.uint8),-1)       
            if 200<img.shape[1]<500 and 200<img.shape[0]<500:
                pass
            elif img.shape[1]<200 and img.shape[0]<200:
                load = load.resize((int(img.shape[1]*3), int(img.shape[0]*3)),Image.ANTIALIAS)
            else:
                load = load.resize((int(img.shape[1]/2), int(img.shape[0]/2)),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)	
            self.L2.config(image=render)
            self.windows.mainloop()	