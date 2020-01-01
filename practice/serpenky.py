from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import *
import time

def triangleinput():
   global x,y,n
   n=3
   x=[0 for p in range(3)]
   y=[0 for q in range(3)]
   for i in range(n):
	x[i]=input("enter x")
	y[i]=input("enter y")
	
def init():
	glClearColor(1.0,1.0,1.0,1.0)
        gluOrtho2D(-100.0,100.0,-100.0,100.0)
	glPointSize(2.0)
	glColor3f(0.0, 1.0, 0.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

def drawSubTriangle( x1,y1,x2,y2,x3,y3):
        #set the colors
        #0, 0 , 0 is black
        #glColor3f(1.0, 1.0, 0.0)
        #draw triangles with midpoints of the original triangle
        glBegin(GL_LINES)
        glVertex2f((x1+x3)/2, (y1+y3)/2)
        glVertex2f((x2+x3)/2, (y2+y3)/2)
        glVertex2f((x2+x3)/2, (y2+y3)/2)
        glVertex2f((x2+x1)/2, (y2+y1)/2)
        glVertex2f((x2+x1)/2, (y2+y1)/2)
        glVertex2f((x1+x3)/2, (y1+y3)/2)
        glEnd()



def drawFractals(x1,y1,x2,y2,x3,y3,c):
        drawSubTriangle(x1,y1,x2,y2,x3,y3)
        #ensure that the size of the triangles is not too small
        #distance formula is in the if condition
        if c>3:
		return
	c+=1
        #drawFractals((x1+x3)/2,(y1+y3)/2, (x3+x2)/2,(y3+y1)/2, x3, y3,c) #top triangle
        drawFractals(x1, y1,(x1+x2)/2, (y1+y2)/2,(x1+x3)/2, (y1+y3)/2,c) #left triangle
        #drawFractals(x1, (x1+x2)/2, (x1+x3)/2, y1, (y1+y2)/2, (y1+y3)/2,c) #left triangle
        #drawFractals((x1+x2)/2, x2, (x3+x2)/2, (y1+y2)/2, y2, (y3+y2)/2,c) #right triangle
        drawFractals((x1+x2)/2, (y1+y2)/2,x2, y2, (x3+x2)/2,(y3+y2)/2,c)#right
        drawFractals((x1+x3)/2, (y1+y3)/2, (x3+x2)/2,(y3+y2)/2,  x3, y3,c)#top
        #drawFractals((x1+x3)/2, x2, (x3+x2)/2, (y1+y3)/2, y2, (y3+y2)/2)


def display():
    triangleinput()
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)
    glVertex2f(x[0], y[0])
    glVertex2f(x[1],y[1])
    glVertex2f(x[1], y[1])
    glVertex2f(x[2], y[2])
    glVertex2f(x[2], y[2])
    glVertex2f(x[0], y[0])
    glEnd()
    drawFractals(x[0], y[0],x[1], y[1], x[2], y[2],1)
    glFlush()




def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(0, 0)
	glutCreateWindow("Seirpenski Triangle")
	#circle()
	glutDisplayFunc(display)
	init()
	glutMainLoop()
main()



"""
himanshu@himanshu-VirtualBox:~/Desktop/practice$ python serpenky.py
enter x-20
enter y-20
enter x100
enter y30
enter x45
enter y85
"""
