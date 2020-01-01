from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def ROUND(a):
	return int(a+0.5)


def setPixel(xcoordinate,ycoordinate):
	glBegin(GL_POINTS)
	glVertex2f(xcoordinate,ycoordinate)
	glEnd()
	glFlush()

def drawDDA(x1,y1,x2,y2):


    dx = x2-x1
    dy = y2-y1
    x,y = x1,y1

    length = dx if abs(dx)>abs(dy) else dy
    length = abs(length)

    xinc = dx/float(length)
    yinc = dy/float(length)

    setPixel(ROUND(x),ROUND(y))
    for i in range(int(length)):
        x += xinc
        y += yinc
        setPixel(round(x),round(y))
