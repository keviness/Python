from turtle import *
def a(lst, l):
    c = []
    for i in lst:
        circle(i, l)
        c.append(i)
    a(c, l)
    
def main():
    setup(1000, 800, 0, 0)
    pensize(2)
    color("red")
    a([12, 78], 38)

main()
        
