from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import time
import datetime
import sys


def init():
    glClearColor(0.0,0.0,0.0,0.0)
    glPointSize(3.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-300.0, 300.0, -300.0, 300.0)

def glut_print(x,y,font,text,r,g,b,a):
    blending=False
    if glIsEnabled(GL_BLEND):
       blending=True
    glEnable(GL_BLEND)
    glColor3f(1.0,1.0,1.0)  
    glRasterPos2f(x,y)
    for ch in text:
      glutBitmapCharacter(font,ctypes.c_int(ord(ch))) 
    if not blending:
      glDisable(GL_BLEND) 
      
  
def draw():
  while True:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    dts=int(time.strftime("%S"))
    dtm=int(time.strftime("%M"))
    dth=int(time.strftime("%H"))
    dtp=time.strftime("%p")
    now=datetime.datetime.now()
    glut_print(-30 ,250,GLUT_BITMAP_TIMES_ROMAN_24,":",1.0,1.0,1.0,1.0)
    glut_print(15 ,250,GLUT_BITMAP_TIMES_ROMAN_24,":",1.0,1.0,1.0,1.0)
    glut_print(-50 ,-250,GLUT_BITMAP_TIMES_ROMAN_24,str(now),1.0,1.0,1.0,1.0)
    s=dts
    mi=dtm
    h=dth
    if(s>9):
       glut_print(35 ,250,GLUT_BITMAP_TIMES_ROMAN_24,str(s),1.0,1.0,1.0,1.0)
    else:
       glut_print(35 ,250,GLUT_BITMAP_TIMES_ROMAN_24,str(0)+str(s),1.0,1.0,1.0,1.0)   
    if(mi>9):
       glut_print(-10,250,GLUT_BITMAP_TIMES_ROMAN_24,str(mi),1.0,1.0,1.0,1.0)
    else:
       glut_print(-10,250,GLUT_BITMAP_TIMES_ROMAN_24,str(0)+str(mi),1.0,1.0,1.0,1.0)  
    if(h>9):
       glut_print(-52,250,GLUT_BITMAP_TIMES_ROMAN_24,str(h),1.0,1.0,1.0,1.0)
    else:
       glut_print(-52,250,GLUT_BITMAP_TIMES_ROMAN_24,str(0)+str(h),1.0,1.0,1.0,1.0) 
    glColor3f(1,1,1)
    glut_print( 70 ,250, GLUT_BITMAP_TIMES_ROMAN_24,dtp, 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print( 70 ,250, GLUT_BITMAP_TIMES_ROMAN_24,dtp, 1.0 , 1.0 , 1.0 , 1.0 ) 
    glutSwapBuffers()         
    
def setPixel(xcor,ycor):
    glBegin(GL_POINTS)
    glVertex2f(xcor,ycor)
    glEnd()
    glFlush()

def keyboard(key,x,y):
   if(key=='q'):
       sys.exit()
       
def Display():
  glClear(GL_COLOR_BUFFER_BIT)
  draw()
  
  
def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(600,600)
  glutInitWindowPosition(50,50)
  glutCreateWindow("Digtal")
  glutDisplayFunc(Display)
  glutKeyboardFunc(keyboard)
  init()
  glutMainLoop()
main()  
  
