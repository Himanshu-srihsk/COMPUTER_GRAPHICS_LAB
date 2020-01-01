from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import time
from math import *
import random
global cir
cir=[]
sys.setrecursionlimit(9999999)
def init():
	glClearColor(1.0,1.0,1.0,1.0)
        gluOrtho2D(0.0,800.0,0.0,800.0)
	glPointSize(2.0)
	#glColor3f(0.0, 1.0, 0.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

def setPixel(xcoordinate,ycoordinate):
    cir.append([xcoordinate,ycoordinate])
    glBegin(GL_POINTS)
    glVertex2f(xcoordinate,ycoordinate)
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

def circle(x,y,r):
	theta=0
	step=0.001
	r*=0.001

	while theta<=pi:
		x += r*cos(theta)
		y += r*sin(theta)
		glBegin(GL_POINTS)
		glVertex2f(x,y)
		glEnd()
		glFlush()
		theta+=step


def flood_input():
	global xf, yf
	print("Enter the flood fill inside point")
	xf = input("x_insidepoint = ")
	yf = input("y_insidepoint = ")
	
def Brescircle(xcenter,ycenter,radius,m):
	x=0
	y=radius
	p=3 - 2*radius
	if m==1:	
	  circlePlotpoints1(xcenter,ycenter,x,y)
	if m==2:	
	  circlePlotpoints2(xcenter,ycenter,x,y)  
        if m==3:	
	  circlePlotpoints3(xcenter,ycenter,x,y)
	if m==4:	
          circlePlotpoints4(xcenter,ycenter,x,y)
	while x <= y:
		x+=1
		if p<0:
			p=p+4*x+6
		else:
			y-=1
			p= p+ 4*(x-y) + 10
		if m==1:	
		  circlePlotpoints1(xcenter,ycenter,x,y)
		if m==2:	
		  circlePlotpoints2(xcenter,ycenter,x,y)  
                if m==3:	
		  circlePlotpoints3(xcenter,ycenter,x,y)
		if m==4:	
		  circlePlotpoints4(xcenter,ycenter,x,y)


def flood(x,y):
  if [int(x),int(y)] not in cir: 
     cir.append([int(x),int(y)])
     setPixel(x,y)
     flood(x+1,y)
     flood(x,y+1) 
     flood(x-1,y) 
     flood(x,y-1) 
    
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
def onMouseclick(button,state,x,y):
	if button==GLUT_LEFT_BUTTON:
		glColor3f(random.uniform(0, 1),random.uniform(0, 1),random.uniform(0, 1))
		#flood_input()
		flood(int(x),int(y))
	elif button==GLUT_RIGHT_BUTTON:
		#glColor3f(1.0,0.0,1.0)
		#drawpoly()
		glColor3f(1.0, 0.3, 1.0)
                glBegin(GL_LINES)                             
                glVertex2f(200, 200)
                glVertex2f(400, 400)
                glVertex2f( 400,200)
                glVertex2f(200, 400)
                glEnd()
                glFlush()
		
def circlePlotpoints(xcenter,ycenter,x,y):
	setPixel(xcenter + x , ycenter + y)
	setPixel(xcenter + x , ycenter - y)
	setPixel(xcenter - x , ycenter + y)
	setPixel(xcenter - x , ycenter - y)
	setPixel(xcenter + y , ycenter + x)
	setPixel(xcenter + y , ycenter - x)
	setPixel(xcenter - y , ycenter + x)
	setPixel(xcenter - y , ycenter - x)

def circlePlotpoints1(xcenter,ycenter,x,y):
	setPixel(xcenter + x , ycenter + y)
	#setPixel(xcenter + x , ycenter - y)
	setPixel(xcenter - x , ycenter + y)
	#setPixel(xcenter - x , ycenter - y)
	setPixel(xcenter + y , ycenter + x)
	#setPixel(xcenter + y , ycenter - x)
	setPixel(xcenter - y , ycenter + x)
	#setPixel(xcenter - y , ycenter - x)
def circlePlotpoints2(xcenter,ycenter,x,y):
	setPixel(xcenter + x , ycenter + y)
	setPixel(xcenter + x , ycenter - y)
	#setPixel(xcenter - x , ycenter + y)
	#setPixel(xcenter - x , ycenter - y)
	setPixel(xcenter + y , ycenter + x)
	setPixel(xcenter + y , ycenter - x)
	#setPixel(xcenter - y , ycenter + x)
	#setPixel(xcenter - y , ycenter - x)
def circlePlotpoints3(xcenter,ycenter,x,y):
	#setPixel(xcenter + x , ycenter + y)
	setPixel(xcenter + x , ycenter - y)
	#setPixel(xcenter - x , ycenter + y)
	setPixel(xcenter - x , ycenter - y)
	#setPixel(xcenter + y , ycenter + x)
	setPixel(xcenter + y , ycenter - x)
	#setPixel(xcenter - y , ycenter + x)
	setPixel(xcenter - y , ycenter - x)
def circlePlotpoints4(xcenter,ycenter,x,y):
	#setPixel(xcenter + x , ycenter + y)
	#setPixel(xcenter + x , ycenter - y)
	setPixel(xcenter - x , ycenter + y)
	setPixel(xcenter - x , ycenter - y)
	#setPixel(xcenter + y , ycenter + x)
	#setPixel(xcenter + y , ycenter - x)
	setPixel(xcenter - y , ycenter + x)
	setPixel(xcenter - y , ycenter - x)				
def display():
    glColor3f(0.8, 0.5, 1.0)
    Brescircle(300,400,100,1)
    lineDDA(200,200,400,200)
    Brescircle(400,300,100,2)
    lineDDA(400,200,400,400)
    Brescircle(300,200,100,3)
    lineDDA(200,400,400,400)
    Brescircle(200,300,100,4)
    lineDDA(200,200,200,400)
    glColor3f(0.7, 0.8, 0.4)
    lineDDA(200,200,400,400)
    lineDDA(200,400,400,200)
    
    
   
    
  
def drawpoly():
    glColor3f(0.0, 0.8, 1.0)
    glBegin(GL_POLYGON)                             
    glVertex2f(200, 200)
    glVertex2f( 400,200)
    glVertex2f(400, 400)
    glVertex2f(200, 400)
    glEnd()
    glFlush()
    glColor3f(1.0, 0.3, 1.0)
    glBegin(GL_LINES)                             
    glVertex2f(200, 200)
    glVertex2f(400, 400)
    glVertex2f( 400,200)
    glVertex2f(200, 400)
    glEnd()
    glFlush()
      
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(0, 0)
	glutCreateWindow("car simulation")
	#circle()
	glutDisplayFunc(display)
	glutMouseFunc(onMouseclick)
	init()
	glutMainLoop()
main()


