#try-绘制进度条

from turtle import *
from time import *
def drawa(wid, length):
    for i in range(2):
        fd(length)
        left(90)
        fd(wid)
        left(90)
def drawb(wid1, m, n):
    begin_fill()
    for i in range(2):
        fd(m)
        left(90)
        fd(wid1)
        left(90)
    end_fill()
def gettime(start):
    s = []
    for i in range(10):
        t = (perf_counter() - start) *10
        sleep(0.1)
        s.append(t)
    return s
def main():
    start = perf_counter()
    setup(1000, 900, 0, 0)
    color("red")
    pensize(2)
    drawa(10, 200)
    c = gettime(start)
    drawb(10, c, 10) 
main()
