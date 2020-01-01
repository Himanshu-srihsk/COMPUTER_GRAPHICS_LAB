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
	glClearColor(0.0, 0.0, 0.0, 0.0)
	gluOrtho2D(-1.0,1.0,-1.0,1.0)
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)
        



    

     
def display():
        glColor3f(1.0, 0.8, 1.0)
        glBegin(GL_POLYGON)        
        glVertex3f( 1.0, 1.0, 0.0 )       
        glVertex3f( 3.0, 2.0, 0.0 )       
        glVertex3f( 3.0, 1.0, 0.0 )        
        glEnd()
        glFlush()
        
    

    
  
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


