from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import datetime
import time
from numpy import *

def init():
  glClearColor(1.0,1.0,1.0,1.0)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  glPointSize(3.0)
  gluOrtho2D(-10.0, 10.0, -10.0, 10.0)

def setPixel(xcor,ycor):
  glBegin(GL_POINTS)
  glVertex2f(xcor,ycor)
  glEnd()
  glFlush()


def drawaxis():
   glColor3f(0.0,0.0,0.0)
   glBegin(GL_LINES)
   glVertex2f(-300.0,0.0)
   glVertex2f(300.0,0.0)
   glVertex2f(0.0,300.0)
   glVertex2f(0.0,-300.0)
   glEnd()
   glFlush()
   
   


 
def Display():
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(0.0,0.0,0.0)
  glPointSize(3.0)
  drawaxis()
  for x in arange(-10.0,10.0,0.05):
     y=cos(x)
     setPixel(x,y)

    
def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(600,600)
  glutInitWindowPosition(50,50)
  glutCreateWindow("SINE SERIES")
  glutDisplayFunc(Display)
  init()
  glutMainLoop()
main()      
