#Circumcircle
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import *
import time
import math

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def init():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-100.0,100.0,-100.0,100.0)
		
def setPixel(xcoordinate,ycoordinate):

    glBegin(GL_POINTS)
    glVertex2f(xcoordinate,ycoordinate)
    glEnd()
    glFlush()


    
def xintersect(midx1,midy1,slope1,midx2,midy2,slope2):
     m1=float(-1/slope1)
     m2=float(-1/slope2)
     xret=(float(midy1-midy2+m2*midx2-m1*midx1)/float(m2-m1))
     return xret


def yintersect(midx1,midy1,slope1,midx2,midy2,slope2):
    m1=float(-1/slope1)
    m2=float(-1/slope2)
    #yret=((m1*m2)/(m1-m2))*(midx1-midx2-float(midy1/m1)+float(midy2/m2))
    yret=(float(m2*midy1-m1*midy2+m1*m2*midx2-m1*m2*midx1)/float(m2-m1))
    return yret


def drawcircle(xcenter,ycenter,radius):
  step = 1/radius   
  for theta in range(360):
		x = xcenter + (radius * cos(theta))
		y = ycenter + (radius * sin(theta))
		setPixel(x,y)
		theta =theta+step


def Brescircle(xcenter,ycenter,radius):
	x=0
	y=radius
	p=3 - 2*radius
	circlePlotpoints(xcenter,ycenter,x,y)
	while x <= y:
		x+=1
		if p<0:
			p=p+4*x+6
		else:
			y-=1
			p= p+ 4*(x-y) + 10
		circlePlotpoints(xcenter,ycenter,x,y)

def circlePlotpoints(xcenter,ycenter,x,y):
	setPixel(xcenter + x , ycenter + y)
	setPixel(xcenter + x , ycenter - y)
	setPixel(xcenter - x , ycenter + y)
	setPixel(xcenter - x , ycenter - y)
	setPixel(xcenter + y , ycenter + x)
	setPixel(xcenter + y , ycenter - x)
	setPixel(xcenter - y , ycenter + x)
	setPixel(xcenter - y , ycenter - x)
	        
def getcircumcentre(ox1,oy1,ox2,oy2,ox3,oy3):
    midx1=float((ox1+ox2)/2.0)
    midy1=float((oy1+oy2)/2.0)
    midx2=float((ox2+ox3)/2.0)
    midy2=float((oy2+oy3)/2.0)
    midx3=float((ox1+ox3)/2.0)
    midy3=float((oy1+oy3)/2.0)
    print (midx1,midy1,midx2,midy2)
    
    slope1,slope2,slope3=0,0,0
    if ox2-ox1 is not 0:
      slope1=(float(oy2-oy1)/float(ox2-ox1))
     
    if ox3-ox2 is not 0:  
      slope2=(float(oy3-oy2)/float(ox3-ox2))
    if ox3-ox1 is not 0:  
      slope3=(float(oy3-oy1)/float(ox3-ox1))
    print (slope1,slope2,slope3)
    
    if (slope1*slope2 ==-1) or  (slope1 ==0 and slope2 ==0):
         print ("hi1")
         xval=midx3
         yval=midy3
    elif (slope3*slope2 ==-1) or  (slope2 ==0 and slope3 ==0):
         print ("hi3")
         xval=midx1
         yval=midy1
              
    elif (slope1*slope3 ==-1) or  (slope1 ==0 and slope3 ==0):
         print ("hi2")
         xval=midx2
         yval=midy2  
     
         
    else:
        print ("hi")
        if slope1 and slope2 is not 0:
          xval=xintersect(midx1,midy1,slope1,midx2,midy2,slope2)
          yval=yintersect(midx1,midy1,slope1,midx2,midy2,slope2)
        if slope2 and slope3 is not 0:
          xval=xintersect(midx2,midy2,slope2,midx3,midy3,slope3)
          yval=yintersect(midx2,midy2,slope2,midx3,midy3,slope3)
        if slope1 and slope3 is not 0:
          xval=xintersect(midx1,midy1,slope1,midx3,midy3,slope3)
          yval=yintersect(midx1,midy1,slope1,midx3,midy3,slope3)   
    
      
             
    print(xval,yval)#circumcenter
    radius=float(math.sqrt((ox1-xval)**2+(oy1-yval)**2))#circumradius
    Brescircle(xval,yval,radius)



		
def display():
 while True:
    ox1=input("x cor1")
    oy1=input("y cor1")
    ox2=input("x cor2")
    oy2=input("y cor2")
    ox3=input("x cor3")
    oy3=input("y cor3")
    
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f( ox1, oy1, 0.0)
    glVertex3f(ox2, oy2, 0.0)
    glVertex3f(ox3, oy3, 0.0)
    glEnd()
    glFlush()
    time.sleep(5)
    getcircumcentre(ox1,oy1,ox2,oy2,ox3,oy3)
    check=int(input("Enter 0 to exit: "))
    if check==0:
	time.sleep(5)
	sys.exit()
    else:
	pass


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(0, 0)
	glutCreateWindow("circumcircle")
	#circle()
	glutDisplayFunc(display)
	init()
	glutMainLoop()
main()		
