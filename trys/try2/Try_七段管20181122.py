# 七段数码管——20181122.py

from turtle import *
from time import *

def drawGap():
    penup()
    fd(5)
def drawLine(draw):
    drawGap()
    pendown() if draw else penup()
    fd(40)
    drawGap()
    right(90)

def drawDigit(digit):
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    
    left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    left(180)
    penup() #为绘制后续数字确定位置
    fd(20) #为绘制后续数字确定位置
    
def drawDate(date):  #data为日期，格式为 '%Y-%m=%d+' 
    pencolor("red")
    for i in date:
        if i == '-':
            write('年',font=("Arial", 18, "normal"))
            pencolor("green")
            fd(40)
        elif i == '=':
            write('月',font=("Arial", 18, "normal"))
            pencolor("blue")
            fd(50)
        elif i == '+':
            write('日',font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i)) 

def main():
    setup(1800, 650, 200, 200)
    penup()
    fd(-300)
    pensize(5)
    drawDate(strftime('%Y-%m+%d+', gmtime()))
    hideturtle()
    done()

main()
             
