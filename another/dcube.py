from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import time

def init():
  glClearColor(1.0,1.0,1.0,1.0)
  glMatrixMode(GL_PROJECTION)
  glPointSize(2.0)
  glColor3f(1.0,0.0,0.0)
  glLoadIdentity()
  gluOrtho2D(-5.0,5.0,-5.0,5.0)
  
def setPixel(xcor,ycor):
  glBegin(GL_POINTS)
  #glVextex2f(xcor,ycor)
  glVertex2f(xcor,ycor)
  glEnd()
  glFlush()

def readcontrolpoints():
  n=input("enter how many ctrl points")
  px=[0 for x in range(n)]
  py=[0 for x in range(n)]
  m=[0 for x in range(n)]
  for x in range(n):
    px[x]=input("ctrl x=")
    py[x]=input("ctrl y=")
    m[x]=input("slope =")
  for i in range(n-1):
    t=0.0
    while(t<=1.0):
      h0=1-3*t*t+2*t*t
      h1=3*t*t-2*t*t*t
      h2=t-2*t*t+t*t*t
      h3=-t*t+t*t*t
      x1=h0*px[i]+h1*px[i+1]+h2*m[i]+h3*m[i+1]
      y1=h0*py[i]+h1*py[i+1]+h2*m[i]+h3*m[i+1]
      setPixel(x1,y1)
      t=t+0.001  
    
def display():
  glClear(GL_COLOR_BUFFER_BIT)
  while True:
     readcontrolpoints()
     check=int(input("Enter 0 to exit"))
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
  glutCreateWindow("Hermite")
  glutDisplayFunc(display)
  init()
  glutMainLoop()
main()   
    


