#Himanshu piechart
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

def init():
	glClearColor(1.0,1.0,1.0,1.0)
        gluOrtho2D(-300.0,300.0,-300.0,300.0)
	glPointSize(2.0)
	
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()




    
def arc(xc,yc,rx,s,e): 
        #angle=s
        #x=rx
        #y=0
        n=float(1)/float(rx)
        ang=float(3.14/180)*s
        end=float(3.14/180)*e
        glBegin(GL_LINE_LOOP)
        while ang<=end:
        	x=xc+rx*math.cos(ang)
        	y=yc+rx*math.sin(ang)
        	glVertex2f(x,y)
        	ang+=n
        #glColor3f(0.0,1.0,0.8)
        #glBegin(GL_LINE_STRIP)
        #glBegin(GL_TRIANGLE_FAN)
        glEnd()
        glFlush()
        
        
#def setpixel(x,y):
     
def display():
   glColor3f(1.0,1.0,0.8)
   glBegin(GL_POLYGON)
   glVertex2f(100,100)
   glVertex2f(220,100)
   glVertex2f(160,204)
   glEnd()
   glFlush()
   arc(100,100,120,0,60)
    
   print "hi1"
   glColor3f(0.2,1.0,0.7)
   arc(100,100,120,60,160)
   print "hi2"
   glColor3f(0.5,1.0,0.8)
   arc(100,100,120,160,220)
   print "hi"
   glColor3f(0.1,0.6,0.1)
   arc(100,100,120,220,360) 
   print "hi1"
    
  
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600, 600)
	glutInitWindowPosition(0, 0)
	glutCreateWindow("PIE CHART ")
	#circle()
	glutDisplayFunc(display)
	init()
	glutMainLoop()
main()


