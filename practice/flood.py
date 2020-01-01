#Himanshu
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import numpy 
from math import *
import time
sys.setrecursionlimit(99999)
global cir
cir=[]

def ROUND(a):
    return int(a + 0.5)


def myInit():
    glClearColor(1.0,1.0,1.0,1.0)
    glPointSize(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-100.0,100.0,-100.0,100.0)


def setPixel(xcoordinate,ycoordinate):
    cir.append([xcoordinate,ycoordinate])
    glBegin(GL_POINTS)
    glVertex2f(xcoordinate,ycoordinate)
    glEnd()
    glFlush()

def lineDDA(x1,y1,x2,y2):
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

def flood_input():
	global xf, yf
	print("Enter the flood fill inside point")
	xf = input("x_insidepoint = ")
	yf = input("y_insidepoint = ")
	    
def inputpoly():
   global n
   n=input("enter no of vertices")
   global polyx,polyy
   polyx=[0 for x in range(n)]
   polyy=[0 for x in range(n)]
   for i in range(n):
      polyx[i]=input("enter x cor:")
      polyy[i]=input("enter y cor:")
   drawpoly(polyx,polyy)   
      

def drawpoly(polyx,polyy):
   glColor3f(1.0,0.0,0.0)
   for i in range(n-1):
      lineDDA(polyx[i],polyy[i],polyx[i+1],polyy[i+1])
   lineDDA(polyx[n-1],polyy[n-1],polyx[0],polyy[0])   
      

def Display():
   inputpoly()
   flood_input()
   


def flood(x,y):
  if [int(x),int(y)] not in cir: 
     cir.append([int(x),int(y)])
     setPixel(x,y)
     flood(x+1,y)
     flood(x,y+1) 
     flood(x-1,y) 
     flood(x,y-1) 
    
      
def onMouseclick(button,state,x,y):
	if button==GLUT_LEFT_BUTTON:
		glColor3f(0.0,1.0,1.0)
		flood(xf,yf)
	elif button==GLUT_RIGHT_BUTTON:
		glColor3f(1.0,0.0,1.0)
		boundary(xs-5,ys+2)	         
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("filling Algorithm")
	glutDisplayFunc(Display)
	time.sleep(5)
	glutMouseFunc(onMouseclick)
	myInit()
	glutMainLoop()

main()


"""
himanshu@himanshu-VirtualBox:~/Desktop/practice$ python flood.py
enter no of vertices4
enter x cor:0
enter y cor:0
enter x cor:100
enter y cor:0
enter x cor:100
enter y cor:100
enter x cor:0
enter y cor:100
Enter the flood fill inside point
x_insidepoint = 50
y_insidepoint = 50
"""

      
         
