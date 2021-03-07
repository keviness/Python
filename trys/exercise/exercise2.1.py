import turtle

def drawSnake(rad, angle, len, neckrad):

    for i in range(len):
        
        turtle.circle(rad, angle)
        turtle.pencolor('green')
        turtle.circle(-rad, angle)
    
        turtle.pencolor('pink')
        turtle.circle(20, 30)
        turtle.pencolor('yellow')

        turtle.circle(-20, 30)
        turtle.pencolor('red')
        
    turtle.fd(rad)
    turtle.circle(rad, angle/2)
        
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad*2)   
   
        
def main():
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 20
    turtle.pensize(pythonsize)
    turtle.pencolor('blue')
    turtle.seth(-30)
    drawSnake(40, 90, 5, pythonsize/2)

main()
