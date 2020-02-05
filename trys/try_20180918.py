
import turtle
import math

def main():

    turtle.setup(1200, 800, 0, 0)
    turtle.pensize(2)
    turtle.color('blue')
    draw(90, 30, 60, 180)

def draw(rad, width, angle1, angle2):
    turtle.seth(0)
    turtle.fd(rad)
    turtle.circle(rad, angle2)
    turtle.seth(-angle1)
    a = math.sqrt(5 * 90)
    turtle.fd(a)

main()


