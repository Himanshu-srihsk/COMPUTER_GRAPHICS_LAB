from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from time import *
from numpy import *
import sys
import time
import math

def init():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glPointSize(5.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-300.0, 300.0, -300.0, 300.0)
	
def setPixel(xcoordinate,ycoordinate):

    glBegin(GL_POINTS)
    glVertex2f(xcoordinate,ycoordinate)
    glEnd()
    glFlush()
    

def inputval():
    global num,r
    num=input("enter no of segments")
    r=input("maximum spiral radius") 
    
def draw_circle():
       
        l=0.0
	for i in range(r):
	    for j in range(720):
	        #theta =float( i/lineAmount*piMultiplier)
	        theta = float(j*3.14)/float(360)
		x = (i+l) * cos(theta)
		y = (i+l) * sin(theta)
		#x = (radius*cos(i*piMultiplier/lineAmount))
		#y = (radius*sin(i*piMultiplier/lineAmount))
		setPixel(x,y)
		l+=0.05
		#radius +=1
		#i+=1
		#theta =theta+step


def keyboard(key, x, y):
    if  key==GLUT_KEY_LEFT:
      draw_circle()
    if  key == GLUT_KEY_RIGHT:
      sys.exit()  


def display():
   glColor3f(1.0, 0.0, 1.0)
   inputval()
   #draw_circle(0.0,0.0,20) 
   
def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(600,600)
  glutInitWindowPosition(50,50)
  glutCreateWindow("spiral")
  glutDisplayFunc(display)
  glutSpecialFunc(keyboard)
  init()
  glutMainLoop()
main()     
