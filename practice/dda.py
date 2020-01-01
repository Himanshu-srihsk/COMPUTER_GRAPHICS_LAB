from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

x0,y0=input("enter 1st ")
x1,y1=input("enter 2nd")
def init():
	glClearColor(1.0, 1.0, 1.0, 1.0)
	gluOrtho2D(-250.0 ,250.0, -250.0, 250.0)


   
def dd():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0, 0.0, 0.0)
	
	
	x=x0
	y=y0
	dx=x1-x0
	dy=y1-y0
	if abs(dx)>abs(dy):
	 steps=abs(dx)
	else:
	 steps=abs(dy)
	xinc=float(dx)/steps
	yinc=float(dy)/steps
	glBegin(GL_POINTS)
	glVertex2f(round(x),round(y))
 	for i in range(1,steps+1):
	 x+=xinc
	 y+=yinc
	 glVertex2f(round(x),round(y))
	glEnd()
	glFlush()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(50,50)
	glutCreateWindow("dda line")	
	glutDisplayFunc(dd)
	init()
	glutMainLoop()
main()

