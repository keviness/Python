# 面向过程程序设计1.py

from math import pi, sin, cos, radians

def main():
    angle = eval(input("Enter the launch angle (degrees):"))
    vel = eval(input("Enter the initial velocity:"))
    h0 = eval(input("Enter the initial height:"))
    time = eval(input("Enter the time interval:"))

xpos = 0
ypos = h0

theat = radians(angle)
xvel = vel * cos(theat)
yvel = vel * sin(theat)

while ypos >= 0:
    xpos = xpos + time * xvel
    yvel1 = yvel - time * 9.8
    ypos = ypos + time * (yvel + yvel1) / 2.0
    yvel = yvel1

print("\n Distance traveled: {0 : 0.1f}meters".format(xpos))

main()
