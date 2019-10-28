import graphics

from graphics import *


# circ = Circle(Point(100, 100), 30)
# win = GraphWin()
# 
# print(circ.draw(win))

## Incrorrect way to create two circles.

leftEye = Circle(Point(80, 50), 5)
leftEye.setFill('yellow')
leftEye.setOutline('red')
rightEye = Circle(Point(100, 50), 5)
rightEye.setFill('yellow')
rightEye.setOutline('red')