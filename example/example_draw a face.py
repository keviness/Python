# draw a face

from graphics import *

win = GraphWin()
face = Circle(Point(100, 95), 50)
leftEye = Circle(Point(80, 80), 5)
leftEye = setFill("yellow")
leftEye = setOutline("red")
rightEye = Circle(Point(120, 80), 5)
rightEye = setFill("yellow")
rightEye = setOutline("red")
mouth = line(Point(80, 110), Point(120, 110))

face.draw(win)
mouth.draw(win)
leftEye(win)
rightEye(win)
