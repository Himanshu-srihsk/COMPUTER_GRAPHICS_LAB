import sys
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
from math import *
from random import *
import copy
sys.setrecursionlimit(9999999)
global cir2,cir1
cir2,cir1=[],[]
def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-250.0,250.0,-250.0,250.0)
def fill_input():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)
	glPointSize(1.0)
	#n=int(input("enter no of vertices "))
	x,y=[],[]
	n=3
	x,y=[-100,0,50],[0,50,-30]
	#x+=[int(input("enter x"+str(1)+" "))]
	#y+=[int(input("enter y"+str(1)+" "))]
	global xs,ys
	xs,ys=x[0]+1,y[0]
	for i in range(1,n):
		#x+=[int(input("enter x"+str(i+1)+" "))]
		#y+=[int(input("enter y"+str(i+1)+" "))]
		dda(x[i-1],y[i-1],x[i],y[i])
	dda(x[n-1],y[n-1],x[0],y[0])
	xs,ys=(min(x)+max(x))/2,(min(y)+max(y))/2
def fill():
	fill_input()
	glColor3f(1.0,0.5,random())
	flood(xs,ys)
def dda(x1,y1,x2,y2):
	dx = x2-x1
	dy = y2-y1
	step=max(abs(dx),abs(dy))*(1.0)
	xinc = dx/step
	yinc = dy/step
	x = x1
	y = y1
	for i in range(int(int(step))):
		glBegin(GL_POINTS)
		glVertex2f(round(x),round(y))
		cir1.append([int(x),int(y)])
		cir2.append([int(x),int(y)])
		x+=xinc
		y+=yinc
		glEnd()
		glFlush()
def flood(x,y):
	if [int(x),int(y)] not in cir1:
		cir1.append([int(x),int(y)])
		glBegin(GL_POINTS)
		glVertex2f(x,y)
		glEnd()
		glFlush()
		flood(x-1,y)
		flood(x+1,y)
		flood(x,y-1)
		flood(x,y+1)
def boundary(x,y):
	if [int(x),int(y)] not in cir2:
		cir2.append([int(x),int(y)])
		glBegin(GL_POINTS)
		glVertex2f(x,y)
		glEnd()
		glFlush()
		#boundary(x-1,y+1)
		#boundary(x+1,y+1)
		#boundary(x-1,y-1)
		#boundary(x+1,y-1)
		boundary(x-1,y)
		boundary(x+1,y)
		boundary(x,y-1)
		boundary(x,y+1)
def onmouse(btn,ste,x,y):
	if btn==GLUT_LEFT_BUTTON:
		glColor3f(0.0,1.0,1.0)
		flood(xs,ys)
	elif btn==GLUT_RIGHT_BUTTON:
		glColor3f(1.0,0.0,1.0)
		boundary(xs-5,ys+2)	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowPosition(400,400)
	glutInitWindowSize(300,300)
	glutCreateWindow("filling")
	init()
	
	glutDisplayFunc(fill)
	fill_input()
	glutMouseFunc(onmouse)
	
	
	glutMainLoop()
main()
