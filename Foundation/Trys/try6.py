import turtle

def main():

    turtle.setup(1300, 800, 0, 0)
    turtle.pensize(10)
    turtle.color('blue')
    
    
    

    draw(190, 80, 60, 120)


def draw(rad, width, angle1, angle2):
    
    turtle.seth(0)
    turtle.fd(rad)
    turtle.seth(angle2)
    turtle.fd(width)
    turtle.seth(180)
    turtle.fd(rad)
    turtle.seth(-angle1)
    turtle.fd(width)


main()
