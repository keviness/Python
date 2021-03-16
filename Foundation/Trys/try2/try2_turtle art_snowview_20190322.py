#try2_turtle art_SnowView_20190322
from turtle import*
from random import *
def drawsnow():
    hideturtle()
    pensize(randint(12,15))
    for i in range(90):
        r, g, b = random(), random(), random()
        pencolor(r, g, b)
        penup()
        setx(randint(-350,350)), sety(randint(1, 250))
        pendown()
        dens = randint(7, 14)
        for j in range(dens):
            fd(randint(11,15))
            backward(randint(10,14))
            right(360/dens)
def drawbackground():
    hideturtle()
    for i in range(395):
        pensize(randint(4, 9))
        x = randint(-400, 340)
        y = randint(-280, -5)
        r, g, b = -y/280, -y/280, -y/280
        pencolor(r, g, b)
        penup()
        goto(x, y)
        pendown()
        fd(randint(40, 100))
def main():
    setup(1200, 900, 0, 0)
    tracer(False)
    bgcolor("black")
    drawsnow()
    drawbackground()
    done()
main()
