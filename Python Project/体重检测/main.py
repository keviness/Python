'''main.py'''
from tkinter import *
from tkinter.ttk import *
from show_pic import Apps
import time
import os
import numpy as np
import tkinter.messagebox
from tkinter import filedialog
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

#将界面定位在屏幕中央
def center_window(top,w, h):
    # 获取屏幕 宽、高
    ws = top.winfo_screenwidth()
    hs = top.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    top.geometry('%dx%d+%d+%d' % (w, h, x, y))

class App:
    def __init__(self):
        self.windos = Tk()
        self.windos.title("体重档案")
        center_window(self.windos,450,400)
        self.lis1 = ["周一", "周二", "周三", "周四", "周五", "周六", "周天"]
        self.images=""
        #self.creat_image_lis()
        self.creat_res()
        self.windos.mainloop()

    #显示万年历    
    def func1(self):
        self.get_total_days(self.a, self.b)
        self.print_days(self.a, self.b)

    #打开子界面
    def open_image(self):
        a1=Apps() 
        if self.windos.quit():#如果主程序关闭
            Apps.windows.quit() #子程序关闭

    #更新折线图
    def view_image(self):
        self.ima=PhotoImage(file=self.images)
        self.L3.config(image=self.ima)

    #显示万年历和折线图
    def go(self,*args):
        self.T1.delete(0.0,END)
        try:
            self.a = int(self.C1.get())
            self.b = int(self.C2.get())
            self.func1()
            
            if self.b<10:
                m="0"+self.C2.get()
            else:
                m=self.C2.get()
            path="res/text/"+self.C1.get()+m+".txt"  #体重记录txt的路径，每月一个文件，如202004.txt
            name=self.C1.get()+m  #年+月，用于文件名

            if not os.path.exists(path):
                tkinter.messagebox.showerror("错误", "数据不存在！")
                return
            #绘制折线图并保存
            values = [] 
            square = []
            data=np.loadtxt(path,delimiter=' ')
            for i in range(len(data)):
                try:
                    values.append(data[i][0])
                    square.append(data[i][1])
                except:
                    tkinter.messagebox.showerror("错误", "只有一天数据！")
                    return
            plt.rcParams['font.sans-serif']=['SimHei']
            plt.plot(values, square, linewidth=5, color='b')  #将列表传递给plot,并设置线宽，设置颜色，默认为蓝色
            plt.title("%s体重变化曲线"%name, fontsize=24, color='r')  
            plt.xlabel("日期", fontsize=14, color='g')  
            plt.ylabel("体重", fontsize=14, color='g')
            plt.tick_params(axis='both', labelsize=14)  #设置刻度标记的大小
            plt.savefig('res/plt/%s.png'%name,dpi=47, bbox_inches='tight')   
            plt.close('all')  #一定是all,否则连tkinter也会关闭；不关闭会接着上次的图继续绘制 
            #更新图片       
            self.images='res/plt/%s.png'%name
            self.view_image()
           
        except Exception:
            tkinter.messagebox.showerror("错误", "请选择年份和月份！")

    #记录体重，以日期+空格+体重的形式逐行写入txt
    def wdown(self):
        if self.E1.get()=='':
            tkinter.messagebox.showerror("错误", "请输入体重！")
            return
        d=time.strftime("%d")
        m=time.strftime("%m")
        y=time.strftime("%Y")   
        date=y+"/"+m+"/"+d     
        path="./"+y+m+".txt"
        if os.path.exists(path):
            data=np.loadtxt(path,delimiter=' ')
            #文档中已有当日记录，则覆盖
            for i in range(len(data)):              	
                try:
                    if int(d) == int(data[i][0]):
                        data[i][1]=int(self.E1.get()) 
                        doc=open(path,"w",encoding='utf8') 
                        for j in range(len(data)):
                            print("%s %s"%(int(data[j][0]),data[j][1]),file=doc)
                        tkinter.messagebox.showinfo(title = '成功！',message='%s数据已记录！'%date)
                        return     
                except:
                    if int(d) == int(data[0]):  #如果txt中只有一行数据，data会变成一维列表
                        data[1]=int(self.E1.get()) 
                        doc=open(path,"w",encoding='utf8') 
                        print("%s %s"%(int(data[0]),data[1]),file=doc)
                        tkinter.messagebox.showinfo(title = '成功！',message='%s数据已记录！'%date)
                        return 
        #不存在当日记录则追加
        txt = d + " "+self.E1.get()+".0"
        with open(path,"a") as doc:      
            doc.write("\n"+txt)
        doc.close()        
        tkinter.messagebox.showinfo(title = '成功！',message='%s数据已记录！'%date)
                
    #初始化tkinter组件
    def creat_res(self):
        self.L1=Label(self.windos,text="年份:")
        self.L2=Label(self.windos,text="月份:")
        self.L3=Label(self.windos)
        self.T1=Text(self.windos)
        self.T1.place(x=10, y=10, width=270, height=150)
        self.B1 = Button(self.windos, text="显示", command=self.go)
        self.B1.place(x=300, y=80)
        self.B2 = Button(self.windos, text="身材相册", command=self.open_image)
        self.B2.place(x=300, y=210)
        self.E1=Entry(self.windos,textvariable="",font="宋体 14")
        self.E1.place(x=300, y=130,width=90,height=20)
        self.B3=Button(self.windos,text="记录体重",command=self.wdown)
        self.B3.place(x=300, y=160)
        self.temp1 = StringVar()
        self.temp2 = StringVar()
        self.C1=Combobox(self.windos,values=[x for x in range(2020,2100)])  #年份的起始在这设置
        self.C2=Combobox(self.windos,values=[x for x in range(1,13)])
        self.C1.place(x=300, y=30, width=60, height=30)
        self.C2.place(x=375, y=30, width=50, height=30)
        self.L1.place(x=300, y=0, width=70, height=30)
        self.L2.place(x=370, y=0, width=50, height=30)
        self.L3.place(x=10, y=170, width=280, height=230)

    #从这开始是万年历的绘制与显示
    def leap_year(self,a):
        if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
            return True
        else:
            return False
    def year_days(self,a,b):
        if b in (1,3,5,8,10,12):
            return 31
        elif b in (4,6,9,11):
            return 30
        else:
            if self.leap_year(self.a)==True:
                return 29
            else:
                return 28
    def get_total_days(self,a,b):
        total_days=0
        for m in range(2020,self.a):  #如果改变了起始年份，这里也要改
            if self.leap_year(m)==True:
                total_days+=366
            else:
                total_days+=365
        for i in range(1,self.b):
            total_days+=self.year_days(self.a,i)
        return total_days
    def get_week(self,a,b):
        return self.get_total_days(self.a,self.b)%7+1
    def print_days(self,a,b):
        self.T1.insert(END,"%s年 %s月"%(self.a,self.b)+"\n")
        self.T1.insert(END," 周一 周二 周三 周四 周五 周六 周天"+"\n")
        self.i=self.get_week(self.a,self.b)
        s=0
        lis1=[x for x in range(1,self.year_days(self.a,self.b)+1)]
        for m in range(1,self.i):
            lis1.insert(0,"  ")
        for i in lis1:
            self.T1.insert(END,"%03s"%i+"  ")
            s+=1
            if s%7==0:
                self.T1.insert(END,"\n")


if __name__ == '__main__':
    ap=App()