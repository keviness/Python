import tkinter
from tkinter import *
import math,time
# 平瑞年
def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

# 月份的天数
def getMonthDays(year, month):
    days = 31
    if month == 2:  # 确定2月天数
        if leap_year(year):
            days = 29
        else:
            days = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:  # 4 6 9 11这些月份均为30天
        days = 30
    return days

# 星期
def getTotalDays(year, month):
    totalDays = 0
    for i in range(1, year):  # 计算从第一年到查询年份的前一年的总天数
        if leap_year(i):
            totalDays += 366
        else:
            totalDays += 365
    for i in range(1, month):  # 再计算查询年份从一月到查询月份的前一个月的天数相加，得到总天数
        totalDays += getMonthDays(year, i)
    return totalDays


# 生成万年历
def f():
    year = t1.get()  # 获取输入框的内容：年份
    month = t2.get()  # 获取输入框的内容：月份
    year = int(year)  # input接受的数据默认为字符串，需要转换为int型
    month = int(month)
    count = 0  # 计数，每7个一换行
    day = []  # 存储万年历的列表
    day.append("日\t一\t二\t三\t四\t五\t六\n\n")
    for i in range((getTotalDays(year, month) % 7) + 1):  # 前面的空出来
        day.append('\t')  # end：可使print输出后不自动换行，接着输出数字
        count += 1
        if count == 7:  # 统一格式
            day.append('\n')
    for i in range(1, getMonthDays(year, month) + 1):  # 输出日期
        day.append(str(i))
        count += 1
        if count % 7 == 0:  # 每7个一换行,不换行则需要\t
            day.append('\n')
        else:
            day.append('\t')
    if count % 7 != 0:  # 如果最后一天不为周六，则将空日期填满（原因：lable默认居中显示）
        for i in range(7 - count % 7 - 1):
            day.append('\t')
        day.append('     ')
    w.config(text="".join(day),bg='pink')  # 更改lable显示内容

    def points():
        for i in range(1,13):
            x = 200 + 130*math.sin(2*math.pi*i/12)
            y = 200 - 130*math.cos(2*math.pi*i/12)
            canvas.create_text(x,y,text=i)

    def createline(radius,line_width,rad):
        global List
        global i
        List = []
        x = 200+radius*math.sin(rad)
        y = 200-radius*math.cos(rad)
        i=canvas.create_line(200,200,x,y,width=line_width)
        List.append(i)

    canvas = tkinter.Canvas(root,width=400,height=500,bd=0,highlightthickness=0)
    canvas.pack()
    canvas.create_oval(50,50,350,350)
    points()

    while 1:
        tm=time.localtime()
        t=time.asctime(tm)
        t_hour=0
        if tm.tm_hour<=12:
            t_hour=tm.tm_hour
        else:
            t_hour=tm.tm_hour-12
        rad1=2*math.pi*(t_hour+tm.tm_min/60)/12
        rad2=2*math.pi*(tm.tm_min+tm.tm_sec/60)/60
        rad3=2*math.pi*tm.tm_sec/60
        createline(50,6,rad1,)
        createline(90,3,rad2)
        createline(120,1,rad3)
        l=canvas.create_text(170,450,text=t)
        root.update()
        time.sleep(1)
        for item in List:
            canvas.delete(item)
            canvas.delete(l)

        root.update()
        mainloop()


# 创建窗口，从窗口键入年份月份，生成万年历
window = tkinter.Tk()  # 创建窗口对象
window.title('万年历')  # 标题
window.minsize(600, 350)  # 窗口大小，设置最大最小值相同，大小可固定
window.maxsize(600, 350)

# 标签、输入框、按钮
show = tkinter.Label(text='', anchor='se', font=('黑体', 30), fg='black')  # 显示框
l1 = tkinter.Label(window, text="请输入年份：")  # 年份
l1.pack()

t1 = tkinter.StringVar()
t1.set('')
entry_year = tkinter.Entry(window, textvariable=t1).pack()

l2 = tkinter.Label(window, text="请输入月份：")  # 月份
l2.pack()
t2 = tkinter.StringVar()
t2.set('')
entry_mon = tkinter.Entry(window, textvariable=t2).pack()



b = tkinter.Button(text='查看万年历', command=f)
b.pack()

# 万年历结果显示在lable中
w = tkinter.Label(window, text=None)
w.pack()

# 显示窗口
window.mainloop()
