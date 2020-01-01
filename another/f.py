from OpenGL.GL import *
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

def init():
   glClearColor(0.0,0.0,0.0,0.0)
   gluOrtho2D(-1.0,1.0,-1.0,1.0)
   glClear(GL_COLOR_BUFFER_BIT)
   glColor3f(1.0,0.0,0.0)
   glPointSize(3.0)
  
def setpixel(x,y):
   glBegin(GL_POINTS)
   glVertex2f(1.0,1.0)
   glEnd()
   glFlush() 
   
def plotpoint():
   setpixel(0.0,0.0)     
   
def main():
   glutInit(sys.argv)
   glutInitWindowSize(500,500)
   glutInitWindowPosition(50,50)
   glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
   glutCreateWindow("point")  
   glutDisplayFunc(plotpoint) 
   init()
   glutMainLoop()
main()
