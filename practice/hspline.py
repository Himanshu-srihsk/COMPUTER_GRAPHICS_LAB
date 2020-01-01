from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from numpy import *
import sys
import time

def init():
 glClearColor(0.0,1.0,1.0,0.0)
 glColor3f(1.0,0.0,0.0)
 glLoadIdentity()
 glMatrixMode(GL_PROJECTION)
 glPointSize(3.0)
 gluOrtho2D(0,1000,0,1000)
 
 
def setPixel(xcor,ycor):
  glBegin(GL_POINTS)
  glVertex2f(xcor,ycor)
  glEnd()
  glFlush()


def B(x,k,i,t):
   if k==1:
      return 1.0 if t[i]<=x<=t[i+1] else 0.0
   if t[i+k-1]==t[i]:
      c1=0.0
   else:
      c1=float((x-t[i])/(t[i+k-1]-t[i])*B(x, k-1, i, t))
      
   if t[i+k]==t[i+1]:
      c2=0.0
   else:
      c2=float((t[i+k]-x)/(t[i+k]-t[i+1])*B(x, k-1, i+1, t))     
   return c1+c2


def read_controlpoints():
   n1=input("enter the numbr of controil points")
   k=input("enter degree")
   n=n1-1
   t=[0 for x in range (n1+k+1)]
   """
   for i in range(n1+k+1):
     if i<k:
       t[i]=0
     elif k<=i<=n:
       t[i]=i-k+1
     else:
       t[i]=n-k+2
     """
   for i in range(n1+k):
     t[i]=input("kont value:")
            
   px=[0 for x in range(n1)]
   py=[0 for x in range(n1)] 
   for i in range(n1):
     px[i]=input("enter control point x")
     py[i]=input("enter control point y")
     setPixel(px[i],py[i])
   
   x=0
   maxu=n-k+2
   while x<=maxu:
      #x1=0.0
      #y1=0.0
      for i in range(n1):
         x1=sum(px[i]*B(x,k,i,t) for i in range(n1))
         y1=sum(py[i]*B(x,k,i,t) for i in range(n1))
         #x1=x1+px[i]*B(x, k, i, t)
         #y1=y1+py[i]*B(x, k, i, t)
      setPixel(x1,y1)
      x+=0.005  
         
  
def display():
  glClear(GL_COLOR_BUFFER_BIT)
  while True:
	read_controlpoints()
	print("Enter any decimal to continue")
	check=int(input("Enter 0 to exit: "))
	if check==0:
		time.sleep(5)
		sys.exit()
	else:
		pass
   
def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(600,600)
  glutInitWindowPosition(50,50)
  glutCreateWindow("Bspline")
  glutDisplayFunc(display)
  init()
  glutMainLoop()
main()  
