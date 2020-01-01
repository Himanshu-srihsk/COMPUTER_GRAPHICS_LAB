#Himanshu Man With Umbrella Walking in the Rain
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import time
from math import *
from numpy import *
import math
import random
sys.setrecursionlimit(99999)
global cir
cir=[]
global ar
ar=[]

#define ScreenWidth getmaxx()
#define ScreenHeight getmaxy()
#define GroundY ScreenHeight*0.75

ScreenWidth=200
ScreenHeight=200
GroundY=200*0.75

def init():
	glClearColor(1.0,1.0,1.0,1.0)
        gluOrtho2D(0.0,200.0,0.0,200.0)
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
  
     
	

def ROUND(x):
   return int(x+0.5)
   	     
def setPixel(xcoordinate,ycoordinate):
    #cir.append([xcoordinate,ycoordinate])
    #glColor3f(1.0,0.0,1.0)
    glBegin(GL_POINTS)
    glVertex2f(xcoordinate,ycoordinate)
    glEnd()
    glFlush()

def setPixelarc(xcoordinate,ycoordinate):
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
        glColor3f(0.0,1.0,0.8)
        glBegin(GL_TRIANGLE_FAN)
        
        for angle in arange(s,e,n):
                x=xc+rx*math.cos(angle)
                y=yc+ry*math.sin(angle)
                glVertex2f(x,y)
                angle+=n      
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



     
def line(x1,y1,x2,y2):

    dx=x2-x1
    dy=y2-y1
    dx1 = abs(x2-x1)
    dy1 = abs(y2-y1)
    x,y=x1,y1
    steps = dx1 if dx1 > dy1 else dy1
    
    xIncrement = dx1/float(steps)
    yIncrement = dy1/float(steps)
    setPixel(ROUND(x),ROUND(y))

    for k in range(int(steps)):

            if dx >= 0:
                x+=xIncrement
            else:
                x-=xIncrement
            if dy >= 0:
                y+=yIncrement
            else:
                y-=yIncrement
            setPixel(ROUND(x),ROUND(y))

def Rain(x,ldisp):
  glColor3f(1.0,0.0,0.0)
  for i in range(400):
     rx=random.randint(0,200) % ScreenWidth
     ry=random.randint(0,200) % ScreenHeight
     print(rx,ry)
     if ry>20:
       if(((rx<10+ldisp or rx>70+ldisp)) or(((rx>10+ldisp and rx<70+ldisp) and ry>80)) ) :
          line(rx,ry,rx+0.5,ry+2)
         
     
  
def DrawManAndUmbrella(x,ldisp):
  glColor3f(1.0,0.0,1.0)
  #head
  Brescircle(20+ldisp,70,10)
  line(20+ldisp,60,20+ldisp,30)
  
  #hand
  line(20+ldisp,50,40+ldisp,50)
  
  #legs
  line(20+ldisp,30,16+ldisp,20)
  #time.sleep(1)
  line(20+ldisp,30,24+ldisp,20)
  
  #umbrella
  glColor3f(0.0,1.0,0.8)
  glBegin(GL_TRIANGLE_FAN)
  glEnd()
  glFlush()
  arc(40+ldisp,80,30,20,0,180)
  line(10+ldisp,80,70+ldisp,80)
  line(40+ldisp,50,40+ldisp,80)
  #flood(40+ldisp,80)
  #time.sleep(4)
       
def display():
   x=0
   ldisp=1
   for i in range(40):
    line(0,20,200,20)
    Rain(x,ldisp)
    DrawManAndUmbrella(x,ldisp)
    ldisp=ldisp+20
    time.sleep(0.06)
    print "hi"
    x=(x+2)%ScreenWidth
    i+=1
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    if ldisp>140:
       ldisp=0
    
  
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600, 600)
	glutInitWindowPosition(0, 0)
	glutCreateWindow("Walking In Rain Animation ")
	#circle()
	glutDisplayFunc(display)
	init()
	glutMainLoop()
main()


