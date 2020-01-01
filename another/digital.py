#Digital watch
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import time
import datetime
import sys

def init():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glPointSize(3.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-300.0, 300.0, -300.0, 300.0)


def glut_print( x,  y,  font,  text, r,  g , b , a):

    blending = False 
    if glIsEnabled(GL_BLEND) :
        blending = True

    glEnable(GL_BLEND)
    glColor3f(1,1,1)
    glRasterPos2f(x,y)
    for ch in text :
        glutBitmapCharacter( font , ctypes.c_int( ord(ch) ) )


    if not blending :
        glDisable(GL_BLEND) 
        
def draw1():
    glColor3f(0.0, 0.8, 1.0)
    glBegin(GL_POLYGON)
    glVertex2f(-400, -400)
    glVertex2f( 400, -200)
    glVertex2f( 200, 400)
    glVertex2f(-400, 400)
    glEnd()
    glFlush()
  
  
def Draw():
  #draw1()

  while True:
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    global dth,dtm,dts,dtp
    dth=int(time.strftime("%H")) 
    dtm=int(time.strftime("%M"))
    dts=int(time.strftime("%S"))
    dtp=time.strftime("%p")
    now=datetime.datetime.now()
    glut_print( -30 ,250, GLUT_BITMAP_TIMES_ROMAN_24 , ":" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print( 15 ,250, GLUT_BITMAP_TIMES_ROMAN_24 , ":" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print( -50 ,-250, GLUT_BITMAP_TIMES_ROMAN_24 ,str(now), 1.0 , 1.0 , 1.0 , 1.0 )
    s=dts
    mi=dtm
    h=dth
    """
    if dts ==0:
	   s=60
           mi=dtm-1
    else:
	   s=dts-1
           mi=dtm
    if dtm==0:
           h=dth-1
    else:
	   h=dth
    if dth>=12:
           h=dth-12
    else:
           h=dth  
    """ 
    #draw1()            
    glColor3f(0,0,0)
    if s>9:
	  glut_print(35 ,250, GLUT_BITMAP_TIMES_ROMAN_24 ,str(s), 1.0 , 1.0 , 1.0 , 1.0 )
    else:  
	  glut_print( 35 ,250, GLUT_BITMAP_TIMES_ROMAN_24 , str(0)+str(s) , 1.0 , 1.0 , 1.0 , 1.0 )
    glColor3f(0,0,0)
    if mi>9:
	  glut_print(-10,250, GLUT_BITMAP_TIMES_ROMAN_24, str(mi) , 1.0 , 1.0 , 1.0 , 1.0 )
    else:  
	  glut_print(-10,250, GLUT_BITMAP_TIMES_ROMAN_24 , str(0)+str(mi) , 1.0 , 1.0 , 1.0 , 1.0 )
    glColor3f(0,0,0)
    if h>9:
	  glut_print(  -52,250, GLUT_BITMAP_TIMES_ROMAN_24 , str(h) , 1.0 , 1.0 , 1.0 , 1.0 )
    else:  
	  glut_print(  -52,250, GLUT_BITMAP_TIMES_ROMAN_24 , str(0)+str(h) , 1.0 , 1.0 , 1.0 , 1.0 )
    glColor3f(1,1,1)
    glut_print( 70 ,250, GLUT_BITMAP_TIMES_ROMAN_24,dtp, 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print( 70 ,250, GLUT_BITMAP_TIMES_ROMAN_24,dtp, 1.0 , 1.0 , 1.0 , 1.0 )           
    # draw my scene ......
    
    glutSwapBuffers()
              
def setPixel(xcoordinate,ycoordinate):

    glBegin(GL_POINTS)
    glVertex2f(xcoordinate,ycoordinate)
    glEnd()
    glFlush()

def keyboard(key, x, y):
    if key == "q":
      sys.exit() 
   
def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	Draw()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Digital")
	glutDisplayFunc(Display)
	glutKeyboardFunc(keyboard)
	init()
	glutMainLoop()

main()
