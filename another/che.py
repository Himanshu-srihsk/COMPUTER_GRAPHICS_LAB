from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import *



class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
        
def ROUND(a):
    return int(a + 0.5)
    
def setPixel(xcoordinate,ycoordinate):

    glBegin(GL_POINTS)
    glVertex2f(xcoordinate,ycoordinate)
    glEnd()
    glFlush()


def lineDDA(x0,y0,xEnd,yEnd):
	delta_x=xEnd-x0
	delta_y=yEnd-y0
	dx=abs(xEnd-x0)
	dy=abs(yEnd-y0)
	x,y=x0,y0
	steps=dx if dx>dy else dy
	if steps !=0:
		change_x=dx/float(steps)
		change_y=dy/float(steps)
	else:
		change_x=0
		change_y=0
	setPixel(x,y)
	
	for k in range(int(steps)):
		if delta_x >= 0:  
			x+=change_x
		else:
			x-=change_x
		if delta_y >= 0:
			y+=change_y
		else:
			y-=change_y
		setPixel(x,y)

"""
def readinput_circle():
	global xcenter,ycenter,radius
	xcenter=input('xCenter:')
	ycenter=input('yCenter:')
	radius=input('Radius:')
"""	
	
	

def init():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0, 500.0, 0.0, 500.0)


def draw_circle(xcenter,ycenter,radius):
	step = 1/radius   
	for theta in range(360):
		x = xcenter + (radius * cos(theta))
		y = ycenter + (radius * sin(theta))
		setPixel(x,y)
		theta =theta+step
	




def display():
	#Terminal Points for Needle
	global pC
	pC = Point(200, 200)
	global radius,pHour,pMinute,pSecond
        radius = 150
        # radius of the needles from  the center
        hRadius = 120
        mRadius = 130
        sRadius = 140
        #angles of the three needles
        hDegree = 0.0
        mDegree = 0.0
        sDegree = 0.0
        pHour=Point(0,0)
        pMinute=Point(0,0)
        pSecond=Point(0,0)
	pHour.y = pC.y + (hRadius * sin(hDegree))
	pHour.x = pC.x + (hRadius * cos(hDegree))

	pMinute.y = pC.y + (mRadius * sin(mDegree))
	pMinute.x = pC.x + (mRadius * cos(mDegree))

	pSecond.y = pC.y + (sRadius * sin(sDegree))
	pSecond.x = pC.x + (sRadius * cos(sDegree))

	glColor3f(1.0, 0.0, 1.0)
	draw_circle(pC.x,pC.y,radius)
	glColor3f(1.0, 0.0, 0.0)
	lineDDA(pC.x,pC.y, pHour.x, pHour.y)

	glColor3f(0.0, 1.0, 0.0)
	lineDDA(pC.x,pC.y, pMinute.x, pMinute.y)

	glColor3f(0.0, 0.0, 1.0)
	lineDDA(pC.x,pC.y,pSecond.x, pSecond.y)
	glEnd()
	glFlush()

	mDegree -= 0.001333333
	sDegree -= 0.08
	hDegree -= 0.0002733333


def Timer(value):
	glutTimerFunc(33, Timer, 0)
	glutPostRedisplay()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(50, 50)
	glutCreateWindow("Analog DigitalS")
	glutDisplayFunc(display)
	init()
	Timer(0)
	glutMainLoop()
main()
