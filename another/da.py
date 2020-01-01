from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

def init():
   glClearColor(1.0,1.0,1.0,1.0)
   gluOrtho2D(-100.0,100.0,-100.0,100.0)
   glClear(GL_COLOR_BUFFER_BIT)
   glColor3f(0.0,0.0,0.0)
   glPointSize(3.0)
x1=input("x1=")
y1=input("y1=")
x2=input("x2=") 
y2=input("y2=") 
def setpixel(x,y):
   glBegin(GL_POINTS)
   glVertex2f(x,y)
   glEnd()
   glFlush()
 
def drawaxis():
   glBegin(GL_LINES)
   glVertex2f(-100.0,0.0)
   glVertex2f(100.0,0.0)
   glVertex2f(0.0,100.0)
   glVertex2f(0.0,-100.0)
   glEnd()
   glFlush()  
   
def drawline():    
   linedda(x1,y1,x2,y2)

def round(x):
   return int(x+0.5)
      
def linedda(x1,y1,x2,y2):
    drawaxis()
    dx=x2-x1
    dy=y2-y1
    if abs(dx)<(dy):
       step=dy
    else:
       step=dx
       
    xinc=dx/step
    yinc=dy/step
    #setpixel(round(xinc),round(yinc))
    for x in range(1,step+1): 
       setpixel(round(x1),round(y1))
       x1+=xinc
       y1+=yinc
      
       
    
         
       
       
         
def main():
   glutInit(sys.argv)
   glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
   glutInitWindowSize(500,500)
   glutInitWindowPosition(50,50)
   glutCreateWindow("line using dda")
   glutDisplayFunc(drawline)
   init()
   glutMainLoop() 
   
main()    
