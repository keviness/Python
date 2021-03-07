import turtle

def drawSnake(rad, angle, len, neckrad):

    for i in range(len):
        
        turtle.circle(rad, angle)
        turtle.pencolor('green')
        turtle.circle(-rad, angle)
    
        turtle.pencolor('pink')
        
    turtle.fd(rad)
    turtle.circle(rad, angle/2)
         
    turtle.circle(neckrad+2, 180)
    turtle.fd(rad*2/3 )   
   
        
def main():
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 20
    turtle.pensize(pythonsize)
    turtle.pencolor('blue')
    turtle.seth(-40)
    drawSnake(40, 90, 9, pythonsize/2)

main()
    

