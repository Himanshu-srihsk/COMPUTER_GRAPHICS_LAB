from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
"""
def init():
   glClearColor(0.0,0.0,0.0,0.0)
   gluOrtho2D(-100.0,100.0,-100.0,100.0)
   glClear(GL_COLOR_BUFFER_BIT)
   glColor(0.7,0.9,0.8)
   glPointSize(4.0)
"""
def init():
	glClearColor(1.0, 1.0, 1.0, 1.0)
	gluOrtho2D(-100.0,100.0,-100.0,100.0)
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)
	   
def setpixel():
   #glColor3f(1.0,.0,0.0)
   glBegin(GL_LINES)
   glVertex2f(-100.0,0.0)
   glVertex2f(100.0,0.0)
   glVertex2f(0.0,100.0)
   glVertex2f(0.0,-100.0)
   glVertex2f(-20,20)
   glVertex2f(20,30)
   glEnd()
   glFlush()
   
def drawline():
  #setpixel(0.0,80.0)
  #setpixel(12.0,120.0)
   setpixel()
   
  
def main():
   glutInit(sys.argv)
   glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
   glutInitWindowSize(500,500)
   glutInitWindowPosition(50,50)
   #glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
   glutCreateWindow("line")
   glutDisplayFunc(setpixel)
   init()
   glutMainLoop()
main()     
