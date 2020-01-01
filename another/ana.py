from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from datetime import *
from time import *
import sys
import time

global hDegree,mDegree,sDegree,PI,xcenter,ycenter,radius
xcenter,ycenter,radius=0.0,0.0,200
hDegree = 20.0
mDegree = 90.0
sDegree = 0.0
PI=3.147
hradius=100
mradius=140
sradius=170
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
    #glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    glColor3f(0,1,1)
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

def readinput_circle():
	global xcenter,ycenter,radius
	xcenter=input('xCenter:')
	ycenter=input('yCenter:')
	radius=input('Radius:')
	
	
	

def init():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-300.0, 300.0, -300.0, 300.0)


def draw_circle(xcenter,ycenter,radius):
        glColor(1.0,0.0,0.0)
	#step = 1/radius   
	for theta in range(360):
	        angle=(3.14*theta)/180
		x = xcenter + (radius * cos(angle))
		y = ycenter + (radius * sin(angle))
		setPixel(x,y)
		theta =theta+0.5
	


def gettime():
        global dth,dtm,dts,dtp
        dth=int(time.strftime("%H")) 
        dtm=int(time.strftime("%M"))
        dts=int(time.strftime("%S"))
        dtp=time.strftime("%p")
        
def second_niddle(dts):
        glColor(0.0,0.0,0.0)
	lineDDA(0,0,-18.164716180901422, 169.02675257505038)
	sx=sradius*cos((90-dts*6+6)*3.14/180) 
	sy=sradius*sin((90-dts*6+6)*3.14/180)
	lineDDA(0,0,sx,sy)
	glColor(1.0,1.0,1.0)
	sx=sradius*cos((90-dts*6)*3.14/180) 
	sy=sradius*sin((90-dts*6)*3.14/180)
	lineDDA(0,0,sx,sy)  

def minute_niddle(mint):
	glColor(0.0,0.0,0.0)
	mx=mradius*cos((90-dtm*6+6)*3.14/180)
	my=mradius*sin((90-dtm*6+6)*3.14/180)
	lineDDA(0,0,mx,my)
	glColor(1.0,1.0,0.0)
	mx=mradius*cos((90-dtm*6)*3.14/180) 
	my=mradius*sin((90-dtm*6)*3.14/180)
	lineDDA(0,0,mx,my)

def hour_niddle(hr):
	glColor(0.0,0.0,0.0)
	hx=hradius*cos((90-dth*30+30)*3.14/180)
	hy=hradius*sin((90-dth*30+30)*3.14/180)
	lineDDA(0,0,hx,hy)
	glColor(1.0,0.0,1.0)
	hx=hradius*cos((90-dth*30)*3.14/180)
	hy=hradius*sin((90-dth*30)*3.14/180)
	lineDDA(0,0,hx,hy)
def clock():
	gettime()
	second_niddle(dts)
        minute_niddle(dtm)
	hour_niddle(dth)
	while True:
		gettime()
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
		"""	
		glColor3f(0,0,0)
		glut_print(10 ,-250, GLUT_BITMAP_9_BY_15 ,str(s), 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(1,1,1)
		glut_print( 10 ,-250, GLUT_BITMAP_9_BY_15 , str(sec) , 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(0,0,0)
		glut_print( -20 ,-250, GLUT_BITMAP_9_BY_15 , str(mi) , 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(1,1,1)
		glut_print( -20 ,-250, GLUT_BITMAP_9_BY_15 , str(mint) , 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(0,0,0)
		glut_print( -50 ,-250, GLUT_BITMAP_9_BY_15 , str(h) , 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(1,1,1)
		glut_print( -50 ,-250, GLUT_BITMAP_9_BY_15 , str(hr) , 1.0 , 1.0 , 1.0 , 1.0 )
		"""
		second_niddle(dts)
		minute_niddle(dtm)
		hour_niddle(dth)
			
def Display():
        global pC
	pC = Point(0.0, 0.0)
	glClear(GL_COLOR_BUFFER_BIT)
	draw_circle(xcenter,ycenter,radius)
	Draw()
	#glut_print(-50 ,-280, GLUT_BITMAP_9_BY_15 ,str(datetime.now().day), 1.0 , 1.0 , 1.0 , 1.0 )
	#glut_print(-30 ,-280, GLUT_BITMAP_9_BY_15 ,"-", 1.0 , 1.0 , 1.0 , 1.0 )
	#glut_print(-20,-280, GLUT_BITMAP_9_BY_15 ,str(datetime.now().month), 1.0 , 1.0 , 1.0 , 1.0 )
	#glut_print(0 ,-280, GLUT_BITMAP_9_BY_15 ,"-", 1.0 , 1.0 , 1.0 , 1.0 )
	#glut_print(10 ,-280, GLUT_BITMAP_9_BY_15 ,str(datetime.now().year), 1.0 , 1.0 , 1.0 , 1.0 )
	clock()
	
def Timer(value):
	glutTimerFunc(33, Timer, 0)
	glutPostRedisplay()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Clock")
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()
