from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
from math import *
import sys
def init():
   glClearColor(1.0, 1.0, 1.0, 1.0)
   gluOrtho2D(-5.0, 5.0, -5.0, 5.0)

def draw_axis():
	glColor3f(0.0,0.0,0.0)
	glBegin(GL_LINES)
	glVertex2f(-300.0,0.0)
	glVertex2f(300.0,0.0)
	glVertex2f(0.0,-300.0)
	glVertex2f(0.0,300.0)
	glEnd()
	glFlush()
	   
def plotfunc():
   glClear(GL_COLOR_BUFFER_BIT)
   glColor3f(0.0, 0.0, 0.0)
   glPointSize(3.0)
   draw_axis()
   for x in arange(-5.0, 5.0, 0.1):
      y = cos(x)
      glBegin(GL_POINTS)
      glVertex2f(x, y)
      glEnd()
      glFlush()  
       
   for x in arange(-5.0, 5.0, 0.1):
      y = sin(x)
      glBegin(GL_POINTS)
      glVertex2f(x, y)
      glEnd()
      glFlush()  
       
def main():
   glutInit(sys.argv)
   glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
   glutInitWindowPosition(50,50)
   glutInitWindowSize(400,400)
   glutCreateWindow("Sine Curve")
   glutDisplayFunc(plotfunc)
   init()
   glutMainLoop()
main()      
