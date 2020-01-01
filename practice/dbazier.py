#BAzier
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from time import *
import sys
import time
import math


def init():
	glClearColor(1.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glPointSize(3.0)
	gluOrtho2D(0,1000,0,800)
	
def setPixel(xcor,ycor):
  glBegin(GL_POINTS)
  glVertex2f(xcor,ycor)
  glEnd()
  glFlush()

		
def factorial(n):
	if n==0:
		return 1
	else:
		n=n*factorial(n-1) 
	return n     
  
def Binomial(n,k):
	result=factorial(n)/(factorial(n-k)*factorial(k))
	return result


def readcontrolpoints():
   global px,py
   n=input("how many control points")
   px=[0 for x in range (n)] 
   py=[0 for x in range (n)]
   for i in range(n):
      px[i]=input("Enter control point_x: ")
      py[i]=input("Enter control point_y: ")
      setPixel(px[i],py[i])
   n=len(px)-1				
   u=0.0
   while u<=1.0:	
	x=0.0
	y=0.0
	for k in range(n+1):		
		x+=Binomial(n,k)*pow(u,k)*pow(1-u,n-k)*px[k]
		y+=Binomial(n,k)*pow(u,k)*pow(1-u,n-k)*py[k]
	setPixel(x,y)		
	u+=0.0001
  
def display():
  while True:
     readcontrolpoints() 
     #Bezier()
     check=int(input("enter 0 to discontinue"))
     if check==0:
	time.sleep(5)
	sys.exit()
     else:
	pass 
  
  
def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(1000,800)
  glutInitWindowPosition(50,50)
  glutCreateWindow("Bazier")
  glutDisplayFunc(display)
  init()
  glutMainLoop()
main()  




"""
enter how many control points are:5
enter control point x4
enter control point y23
enter control point x56
enter control point y85
enter control point x12
enter control point y55
enter control point x89
enter control point y65
enter control point x41
enter control point y35
"""   
