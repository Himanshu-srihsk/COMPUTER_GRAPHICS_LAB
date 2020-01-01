from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import *
import time

global hDegree,mDegree,sDegree,PI
hDegree = 20.0
mDegree = 90.0
sDegree = 0.0
PI=3.147
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
        
def ROUND(a):
    return int(a + 0.5)
    
def setPixel(xcoordinate,ycoordinate):

    glBegin(GL_POINTS)
    glVertex2f(xcoordinate,ycoordinate)
    glEnd()
    glFlush()


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
        


def Draw():
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    
    glut_print( pC.x+95+(-5) ,pC.y-165+(-5) , GLUT_BITMAP_9_BY_15 , "5" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(pC.x+165+(-5),pC.y-95+(-5), GLUT_BITMAP_9_BY_15 , "4" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print( pC.x+190+(-5),pC.y+0+(-7) , GLUT_BITMAP_9_BY_15 , "3" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print( pC.x+165+(-7),pC.y+95+(-7) , GLUT_BITMAP_9_BY_15 , "2" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(pC.x+95+(-5),pC.y+165+(-10), GLUT_BITMAP_9_BY_15 , "1" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print( pC.x+0+(-3),pC.y+190+(-10), GLUT_BITMAP_9_BY_15 , "12" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print( pC.x-95+(0),pC.y+165+(-10), GLUT_BITMAP_9_BY_15 , "11" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print( pC.x-165+(-2),pC.y+95+(-10), GLUT_BITMAP_9_BY_15 , "10" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print( pC.x-190+(-3),pC.y+0+(-7) , GLUT_BITMAP_9_BY_15 , "9" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print( pC.x-165+(-5),pC.y-95+(-3) , GLUT_BITMAP_9_BY_15 , "8" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print( pC.x-95+(-5),pC.y-165+(-5), GLUT_BITMAP_9_BY_15 , "7" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print( pC.x+0+(-6),pC.y-190+(-5), GLUT_BITMAP_9_BY_15 , "6" , 1.0 , 1.0 , 1.0 , 1.0 )
    # draw my scene ......
    glutSwapBuffers()
    
    
def lineDDA(x0,y0,xEnd,yEnd):
	delta_x=xEnd-x0
	delta_y=yEnd-y0
	dx=abs(xEnd-x0)
	dy=abs(yEnd-y0)
	x,y=x0,y0
	steps=dx if dx>dy else dy
	if steps !=0:
		change_x=dx/float(steps)
		change_y=dy/float(steps)
	else:
		change_x=0
		change_y=0
	setPixel(x,y)
	
	for k in range(int(steps)):
		if delta_x >= 0:  
			x+=change_x
		else:
			x-=change_x
		if delta_y >= 0:
			y+=change_y
		else:
			y-=change_y
		setPixel(x,y)


"""
def readinput_circle():
	global xcenter,ycenter,radius
	xcenter=input('xCenter:')
	ycenter=input('yCenter:')
	radius=input('Radius:')
"""	
	
	

def init():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-300.0, 300.0, -300.0, 300.0)


def draw_circle(xcenter,ycenter,radius):
	step = 1/radius   
	for theta in range(360):
		x = xcenter + (radius * cos(theta))
		y = ycenter + (radius * sin(theta))
		setPixel(x,y)
		theta =theta+step
	



def circle():
        global pC,radius
	pC = Point(200, 200)
	#global radius,hDegree,sDegree,mDegree
        radius = 200
        # radius of the needles from  the center
        #hRadius = 90
        #mRadius = 140
        #sRadius = 170
        glColor3f(1.0, 0.0, 1.0)
	draw_circle(pC.x,pC.y,radius)
	Draw()
	
	
def display():
	#Terminal Points for Needle
	global pC
	pC = Point(0, 0)
	global radius,hDegree,sDegree,mDegree
        radius = 200
        # radius of the needles from  the center
        hRadius = 90
        mRadius = 140
        sRadius = 170
        #angles of the three needles
       
        #pHour=Point(0,0)
        #pMinute=Point(0,0)
        #pSecond=Point(0,0)
        global pHour
	pHour=Point(pC.x + (hRadius * cos(hDegree)),pC.y + (hRadius * sin(hDegree)))
	#pHour.x = pC.x + (hRadius * cos(hDegree))
	global pMinute
	pMinute = Point(pC.x + (mRadius * cos(mDegree)),pC.y + (mRadius * sin(mDegree)))
	#pMinute.x = pC.x + (mRadius * cos(mDegree))
	global pSecond
	pSecond= Point(pC.x + (sRadius * cos(sDegree)),pC.y + (sRadius * sin(sDegree)))
	#pSecond.x = pC.x + (sRadius * cos(sDegree))
        
	glColor3f(1.0, 0.0, 1.0)
	draw_circle(pC.x,pC.y,radius)
	Draw()

        
	glColor3f(1.0, 0.0, 0.0)
	lineDDA(pC.x,pC.y, pHour.x, pHour.y)

	glColor3f(0.0, 1.0, 0.0)
	lineDDA(pC.x,pC.y, pMinute.x, pMinute.y)

	glColor3f(0.0, 0.0, 1.0)
	lineDDA(pC.x,pC.y,pSecond.x, pSecond.y)
        glFlush()
	"""
        while(True):
              sDegree += 6.0
              if(sDegree == 360.0):
	          sDegree = 0.0
	          mDegree += 6.0
	          hDegree += (1.0/12.0 * mDegree)
	      if(mDegree == 360.0):
		  mDegree = 0.0
		  hDegree+=6.0

	      if(hDegree == 360.0):
		  hDegree = 0.0
	      pSecond= Point(pC.x + (sRadius * cos(sDegree)),pC.y + (sRadius * sin(sDegree)))	      
	      pMinute = Point(pC.x + (mRadius * cos(mDegree)),pC.y + (mRadius * sin(mDegree)))		
	      pHour=Point(pC.x + (hRadius * cos(hDegree)),pC.y + (hRadius * sin(hDegree)))
       """
        dth=time.strftime("%H") 
        dtm=time.strftime("%M")
        dts=time.strftime("%S")
        dtp=time.strftime("%p")
        #O=(dts*(PI/30)-(PI/2))
        #lineDDA(0/2,pC.y/2,pC.x+radius*cos(O),pC.y+radius*sin(O))   
        #mDegree +=0.1
	#sDegree -=6
	#hDegree += 0.008333
	mDegree +=0.001333333
	sDegree +=0.08
	hDegree +=0.0002733333
        print(hDegree,mDegree,sDegree,dth,dtm,dts,dtp)

def Timer(value):
	glutTimerFunc(5, Timer, 0)
	glutPostRedisplay()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(50, 50)
	glutCreateWindow("Analog DigitalS")
	#circle()
	glutDisplayFunc(display)
	init()
	Timer(0)
	glutMainLoop()
main()
