# not working for input line[[20,20],[250,180]], sq region [[50,50],[200,200]]
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from time import *
import time

INSIDE = 0 	#0000
LEFT = 1   	#0001
RIGHT = 2  	#0010
BOTTOM = 4 	#0100
TOP = 8    	#1000
global tx,ty,t1x,t1y

def ROUND(a):
	return int(a+0.5)

def setPixel(x,y):
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glFlush()

"""
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

def breshman(x0, y0, x1, y1):

	# ALL CASES

	dx = x1 - x0
	dy = y1 - y0

	xsign = 1 if dx > 0 else -1
	ysign = 1 if dy > 0 else -1

	dx = abs(dx)
	dy = abs(dy)

	if dx > dy:
		xx, xy, yx, yy = xsign, 0, 0, ysign

	else:
		dx, dy = dy, dx
		xx, xy, yx, yy = 0, ysign, xsign, 0

	D = 2*dy - dx
	y = 0

	for x in range(dx + 1):
		setPixel(x0 + x*xx + y*yx, y0 + x*xy + y*yy)
		if D >= 0:
			y += 1
			D -= 2*dx
		D += 2*dy

def init():
  glClearColor(0.0,0.0,0.0,0.0)
  glMatrixMode(GL_PROJECTION)
  glPointSize(2.0)
  glColor3f(1.0,0.0,0.0)
  glLoadIdentity()
  gluOrtho2D(0.0,600.0,0.0,600.0)

def drawRectangle():
  glColor3f(1.0,0.0,0.0)
  breshman(xmin,ymin,xmax,ymin)
  breshman(xmax,ymin,xmax,ymax)
  breshman(xmax,ymax,xmin,ymax)
  breshman(xmin,ymax,xmin,ymin)

def readwindow():
  global xmin,ymin,xmax,ymax
  xmin=input("enter xmin:")
  ymin=input("enter ymin:")
  xmax=input("enter xmax:")
  ymax=input("enter ymax:")


def computecode(x,y):
   code=INSIDE
   if x<xmin:
      code=code|LEFT
   elif x>xmax:
      code=code|RIGHT
   if y<ymin:
      code=code|BOTTOM
   elif y>ymax:
      code=code|TOP        
   return code
  
  
def cohensoutherlandclip(x1,y1,x2,y2,tx,ty,t1x,t1y):
  code1=computecode(x1,y1)
  code2=computecode(x2,y2)
  accept=False
  
  while True:
    if code1==0 and code2 == 0:
			accept = True
			glColor3f(0.0,0.0,0.0)
			breshman(tx,ty,t1x,t1y)
			break
    elif(code1 & code2) !=0:
       break
    else:
       x=0.0
       y=0.0
       dx=x2-x1
       dy=y2-y1
       if dx != 0:       # for handling divide by 0
	  m=dy/dx
       if code1 != 0:
	  code_out = code1
       else:
	  code_out = code2
       
       if code_out & TOP:
          y=ymax
          if dx == 0:         # when slope of line is infinity or undefined
	     x=x1
	  else:   
             x=x1+(ymax-y1)/m
          
       elif code_out & BOTTOM:
          y=ymin
          if dx == 0:         # when slope of line is infinity or undefined
	     x=x1
          else:
             x=x1+(ymin-y1)/m 
                	  
       elif code_out & RIGHT:
          x=xmax
          y=y1+m*(xmax-x1)
          
       elif code_out & LEFT:
          x=xmin
          y=y1+m*(xmin-x1)
       
       if code_out == code1:
		x1=x
		y1=y
		code1=computecode(x1,y1)
       else:
		x2=x
		y2=y
		code2=computecode(x2,y2)

       
  if accept:
		print(x1,y1,x2,y2)
		glColor3f(1.0,0.0,0.0)
		breshman(ROUND(x1),ROUND(y1),ROUND(x2),ROUND(y2))
  else:
		print("Line is rejected")

  
def readinput():
	x1 = input("Enter 1st x-coordinate")
	y1 = input("Enter 1st y-coordinate")
	x2 = input("Enter 2nd x-coordinate")
	y2 = input("Enter 2nd y-coordinate")
	tx=x1
	ty=y1
	t1x=x2
	t1y=y2
	glColor3f(1.0,0.0,0.0)
	breshman(x1,y1,x2,y2)
	while True:
		readwindow()
		drawRectangle()
		time.sleep(5)
		cohensoutherlandclip(x1,y1,x2,y2,tx,ty,t1x,t1y)
		print("Enter a decimal no other than 0 to continue")
		check=int(input("Enter 0 to exit: "))
		if check == 0:
		        time.sleep(3)
			sys.exit()
		else:
			pass    
  
  
def display():
  readinput()  
  	
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
      	
  	
