#Himanshu Car Simulation
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import time

def init():
	glClearColor(1.0,1.0,1.0,1.0)
        gluOrtho2D(0.0,800.0,0.0,800.0)
	glPointSize(2.0)
	#glColor3f(0.0, 1.0, 0.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

def setPixel(xcoordinate,ycoordinate):

    glBegin(GL_POINTS)
    glVertex2i(xcoordinate,ycoordinate)
    glEnd()
    glFlush()
    
def draw1():
    glColor3f(0.0, 0.8, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, -0.5)
    glVertex2f( 0.5, -0.5)
    glVertex2f( 0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()
    glFlush()


def Brescircle(xcenter,ycenter,radius):
	x=0
	y=radius
	p=3 - 2*radius
	circlePlotpoints(xcenter,ycenter,x,y)
	while x <= y:
		x+=1
		if p<0:
			p=p+4*x+6
		else:
			y-=1
			p= p+ 4*(x-y) + 10
		circlePlotpoints(xcenter,ycenter,x,y)

def circlePlotpoints(xcenter,ycenter,x,y):
	setPixel(xcenter + x , ycenter + y)
	setPixel(xcenter + x , ycenter - y)
	setPixel(xcenter - x , ycenter + y)
	setPixel(xcenter - x , ycenter - y)
	setPixel(xcenter + y , ycenter + x)
	setPixel(xcenter + y , ycenter - x)
	setPixel(xcenter - y , ycenter + x)
	setPixel(xcenter - y , ycenter - x)

def display():
  for i in range(1,800):
    glColor3f(0.0, 0.8, 1.0)
    glBegin(GL_POLYGON)                             
    glVertex2f(50+i, 275)
    glVertex2f( 150+i,275)
    glVertex2f(150+i, 400)
    glVertex2f(50+i, 400)
    glEnd()
    glFlush()
    glColor3f(0.0, 0.8, 1.0)
    glBegin(GL_POLYGON)                             
    glVertex2f(150+i, 350)
    glVertex2f(200+i,350)
    glVertex2f(200+i, 400)
    glVertex2f(150+i, 400)
    glEnd()
    glFlush()
    Brescircle(75+i,410,10)
    Brescircle(175+i,410,10)
    time.sleep(2)
    glClear(GL_COLOR_BUFFER_BIT)
    i=i*2
    
    
  
  
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(0, 0)
	glutCreateWindow("car simulation")
	#circle()
	glutDisplayFunc(display)
	init()
	glutMainLoop()
main()


