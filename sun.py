#sun
from OpenGL.GL  import *
from OpenGL.GLU  import *
from OpenGL.GLUT  import *
import sys
import numpy
from math import *
from numpy import *
import time
import random
def init():
  glClearColor(0.0,1.0,1.0,1.0)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  glPointSize(2.0)
  gluOrtho2D(-100,100,-100,100)
  
def setpixel(x,y):
  glBegin(GL_POINTS)
  glVertex2f(x,y)
  glEnd()
  glFlush()
  

def drawcircle(xc,yc,r):
  x,y=0,0
  glBegin(GL_POINTS)
  glVertex2f(x,y)
  for theta in arange (0,360,0.5):
    theta=float((3.14*theta)/180)
    x=xc+r*cos(theta)
    y=yc+r*sin(theta)
    glVertex2f(x,y)
  glEnd()
  glFlush()

def animate():
   glClear(GL_COLOR_BUFFER_BIT)
   t=0
   for i in range(100):
     drawcircle(0,0,25) 
     drawcircle(0,0,15)
     drawcircle(0,0,5)
     drawhand(t) 
     t+=50
     time.sleep(1)
     glClear(GL_COLOR_BUFFER_BIT)
     
def drawaxis():
  glBegin(GL_LINES)
  glVertex2f(-100,0)
  glVertex2f(100,0)
  glVertex2f(0,-100)
  glVertex2f(0,100)
  glEnd()
  glFlush()
def drawhand(t):

 r=25
 th=0
 for i in range(11): 
  glColor3f(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
  theta1=float(3.14*(23+th+t)/180)
  x1=r*cos(theta1)
  y1=r*sin(theta1)
  theta2=float(3.14*(-22+th+t)/180)
  x2=r*cos(theta2)
  y2=r*sin(theta2)
  glBegin(GL_POLYGON)
 
  thetaavg=(theta1+theta2)/2   
  r2=(r+20)*sin(thetaavg) 
  r1=(r+20)*cos(thetaavg) 
  glVertex2f(x1,y1)
  glVertex2f(r1,r2)    
  glVertex2f(x2,y2)
  glVertex2f(r1,r2)
  th+=45
  glEnd()
  glFlush()
    
def display():
  #glColor3f(1.0,1.0,0.0)
  #drawaxis()
  glColor3f(1.0,0.0,0.0)
  drawcircle(0,0,25)  
  drawhand(0)

def keyboard(key, x, y):
  if key == "a":
      animate()
      print "click"
  if key == "q":
      sys.exit() 
      print "exit"  
        
def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(600,600)
  glutInitWindowPosition(50,50)
  glutCreateWindow("sun")
  glutDisplayFunc(display)
  glutKeyboardFunc(keyboard)
  glutIdleFunc(animate)
  init()
  glutMainLoop()
main()      
  

