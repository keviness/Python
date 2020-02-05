# try-turtle 绘制进度条20181209.py

from turtle import *

def c(plist, l):
    lst = []
    for a in plist:
        a.forward(l)
        b = a.clone()
        lst.append(a)
        lst.append(b)
    c(lst, l)
def main():
    setup(1000, 900, 1, 1)
    color("red")
    pensize(2)
    c([a], 46)

main()
        
        
