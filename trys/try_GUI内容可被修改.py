# 内容可被修改 2018.10.30

from graphics import *

win = GraphWin("Celsius Converter", 400, 300)
win.setCoords(0.0, 0.0, 4.0, 4.0)

Text(Point(1, 3), "Celsius Temperature:").draw(win)
Text(Point(2, 3), "C").draw(win)
Text(Point(1, 1), "Fahrenheit Temperature:").draw(win)
Text(Point(2.5, 1), "F").draw(win)
input = Entry(Point(2, 3), 5)
input.setText("0.0")
input.draw(win)

output = Text(Point(2, 1), "")
output.draw(win)

button = Text(Point(1.5, 2.0), "Convert It")
button.draw(win)

Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)
win.getMouse()

celsius = eval(input.getText())
fahrenheit = 9.0/5.0 * celsius + 32.0

output.setText(fahrenheit)
button.setText("Quit")

win.getMouse()
win.close()
