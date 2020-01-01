#Himanshu Smiling Face Animation
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import time
from math import *
from numpy import *
import math
sys.setrecursionlimit(99999)
global cir
cir=[]
global ar
ar=[]
def init():
	glClearColor(1.0,1.0,1.0,1.0)
        gluOrtho2D(-200.0,200.0,-200.0,200.0)
	glPointSize(2.0)
	
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

def flood(x,y):
  if [int(x),int(y)] not in cir: 
     cir.append([int(x),int(y)])
     glBegin(GL_POINTS)
     glVertex2f(x,y)
     glEnd()
     flood(x+1,y)
     flood(x,y+1) 
     flood(x-1,y) 
     flood(x,y-1)
  
     

def flood_input():
	global xf, yf
	print("Enter the flood fill inside point")
	xf = input("x_insidepoint = ")
	yf = input("y_insidepoint = ")
	
	     
def setPixel(xcoordinate,ycoordinate):
    cir.append([xcoordinate,ycoordinate])
    glBegin(GL_POINTS)
    glVertex2f(xcoordinate,ycoordinate)
    glEnd()
    glFlush()


    
def arc(xc,yc,rx,ry,s,e): 
        angle=0
        x=rx
        y=0
        n=float(1)/float(rx)
        s=float(3.14*float(s/180))
        e=float(3.14*float(e/180))
        for angle in arange(s,e,n):
                x=xc+rx*math.cos(angle)
                y=yc+ry*math.sin(angle)
                setPixel(x,y)
                angle+=n      
                    
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



def smiley(xf, yf,radius):
    
     glColor3f(1.0, 0.0, 0.0)
     Brescircle(xf- 30, yf +30,radius/6)#arc(xf- 30, yf +30, 10, 15,0,360)
     glColor3f(1.0, 0.0, 0.0)
     flood(xf- 30, yf +30)
     glColor3f(1.0, 0.0, 0.0)
     Brescircle(xf+ 30, yf +30,radius/6)#arc(xf+30, yf +30, 10, 15,0,360)
     glColor3f(1.0, 0.0, 0.0)
     flood(xf+30, yf +30)
     
     glColor3f(1.0, 1.0, 0.0)
     Brescircle(xf,yf,radius)
     glColor3f(1.0, 1.0, 0.0)
     flood(xf,yf)
     glColor3f(0.0, 0.0, 0.0)
     glBegin(GL_POLYGON)
     glVertex2f(0.0,15.0)
     glVertex2f(-5.0,-6.0)
     glVertex2f(5.0,-6.0)
     glEnd()
     glFlush()
     print ar
     
        
     
      
def display():
    for i in range(3):
        smiley(0,0,60)
        glColor3f(0.0,0.0,0.0)
        glBegin(GL_LINES)
        glVertex2f(-25.0,-25.0)
        glVertex2f(25.0,-25.0)
        glEnd()
        glFlush()
        time.sleep(1)
        
        glClear(GL_COLOR_BUFFER_BIT)
        
        smiley(0,0,60)
        arc(0, -25.0,25.0,20.0,0, 180)
        time.sleep(1)
        
        glClear(GL_COLOR_BUFFER_BIT)
        
        smiley(0,0,60)
        arc(0, -25.0,20.0,20.0,180, 360)
        time.sleep(1)
        
        glClear(GL_COLOR_BUFFER_BIT)
        
        smiley(0,0,60)
        glBegin(GL_LINES)
        glVertex2f(-25.0,-25.0)
        glVertex2f(25.0,-25.0)
        glEnd()
        glFlush()
        arc(0, -25.0,25.0,3.0,180, 360)
        time.sleep(1)
        
        glClear(GL_COLOR_BUFFER_BIT)
        
        smiley(0,0,60)
        glBegin(GL_LINES)
        glVertex2f(-25.0,-25.0)
        glVertex2f(25.0,-25.0)
        glEnd()
        glFlush()
        arc(0, -25.0,25.0,10.0,180, 360)
        time.sleep(1)
        
        glClear(GL_COLOR_BUFFER_BIT)
        
        smiley(0,0,60)
        glBegin(GL_LINES)
        glVertex2f(-25.0,-25.0)
        glVertex2f(25.0,-25.0)
        glEnd()
        glFlush()
        arc(0, -25.0,25.0,15.0,180, 360)
        time.sleep(1)
        glClear(GL_COLOR_BUFFER_BIT)
        
        smiley(0,0,60)
        glBegin(GL_LINES)
        glVertex2f(-25.0,-25.0)
        glVertex2f(25.0,-25.0)
        glEnd()
        glFlush()
        arc(0, -25.0,25.0,18.0,180, 360)
        time.sleep(1)
        glClear(GL_COLOR_BUFFER_BIT)
        
        smiley(0,0,60)
        glBegin(GL_LINES)
        glVertex2f(-25.0,-25.0)
        glVertex2f(25.0,-25.0)
        glEnd()
        glFlush()
        arc(0, -25.0,25.0,22.0,180, 360)
        time.sleep(1)
        
        glClear(GL_COLOR_BUFFER_BIT)
       
    
  
    
    
  
  
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(0, 0)
	glutCreateWindow("Smiling Face ")
	#circle()
	glutDisplayFunc(display)
	init()
	glutMainLoop()
main()


