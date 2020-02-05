import turtle

def main():
    turtle.setup(1300, 800, 0, 0 )
    turtle.pensize(4)
    turtle.color('red')
    turtle.seth(90)
    drawCircle(130, 360)

def drawCircle(rad, angle,):
    for i in range(2):
        turtle.color('green')
        turtle.circle(rad, angle)
        turtle.color('blue')
        turtle.circle(-rad, angle)
        
        
    
        turtle.seth(90)
        turtle.fd(rad)
    turtle.seth(-30)
    turtle.fd(2*rad)
    turtle.seth(-150)
    turtle.fd(2*rad)


    
main()
