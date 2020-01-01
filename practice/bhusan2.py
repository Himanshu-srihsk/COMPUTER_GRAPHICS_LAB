#Bhusanwa ka swal # Ellipse create to form cylinder and rotate it
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys
import math
import time
matrix=[[0 for x in range(1)] for y in range(3)]    # 3*1 matrix to store homogenious point (x,y)
composite_matrix=[[0 for x in range(3)] for y in range(3)]  # 3*3 composite matrix

def setidentity(m):
   for x in range(3):
      for y in range(3):
         if x==y:
             m[x][y]=1

def matrix_multiply(matrix_a,matrix_b):
   temp_matrix=[[0 for x in range(3)] for y in range(3)]
   for i in range(len(matrix_a)):
		for j in range(len(matrix_b[0])):
			for k in range(len(matrix_a)):
				temp_matrix[i][j]+=matrix_a[i][k]*matrix_b[k][j]
				
   for i in range(len(matrix_b)):
		for j in range(len(matrix_b[0])):
			matrix_b[i][j]=temp_matrix[i][j]				

def translate(tx,ty):
   m=[[0 for x in range(3)] for y in range(3)]
   setidentity(m)
   m[0][2]=tx
   m[1][2]=ty
   matrix_multiply(m,composite_matrix)
   
   
   
                   
def ROUND(a):
    return int(a + 0.5)

def init():
  glClearColor(1.0,1.0,1.0,1.0)
  glMatrixMode(GL_PROJECTION)
  glClear(GL_COLOR_BUFFER_BIT)
  glPointSize(3.0)
  gluOrtho2D(-800.0, 800.0, -800.0, 800.0)

def setPixel(xcor,ycor):
  glBegin(GL_POINTS)
  glVertex2f(xcor,ycor)
  glEnd()
  glFlush()


def drawaxis():
   glColor3f(0.0,0.0,0.0)
   glBegin(GL_LINES)
   glVertex2f(-800.0,0.0)
   glVertex2f(800.0,0.0)
   glVertex2f(0.0,800.0)
   glVertex2f(0.0,-800.0)
   glEnd()
   glFlush()
   
def draw(xc,yc,tx,ty): 
     
     x=rx
     y=0
     n=float(1)/float(rx)
     for j in range(6):
	    xc=xc+tx
	    yc=yc+ty
	    angle=0
         while angle<=2*3.14 :
                x=xc+rx*math.cos(angle)
                y=yc+ry*math.sin(angle)
                setPixel(x,y)
                angle+=n    
                
          j+=1

def ellipse(): 
        angle=0
        rx=200
        ry=180
        n=float(1)/float(rx)
        glColor3f(0.0,1.0,0.8)
        glBegin(GL_LINE_LOOP)
   
        for i in range(360) :
                angle=float(i*float(3.14/180))
                x=rx*math.cos(angle)
                y=ry*math.sin(angle)
                glVertex2f(x,y)
                #angle+=n   
        glEnd()
        glFlush()

def rotate(theta,refpoint_x,refpoint_y):
	tx=refpoint_x - 0
	ty=refpoint_y - 0
	translate(-tx,-ty)
	m=[[0 for x in range(3)] for y in range(3)]
	setidentity(m)
	theta=3.14159*(theta/180)
	m[0][0]=cos(theta)
	m[0][1]=-sin(theta)
	m[1][0]=sin(theta)
	m[1][1]=cos(theta)
	matrix_multiply(m,composite_matrix)
	translate(tx,ty)      
	                  
def drawellipse():
        global rx,ry,xc,yc
        xc,yc=input("enter the centre of ellipse:  ")
        rx,ry=input("enter the major and minor axis: ")
        tx,ty=input("enter tx,ty:")
        #draw(xc,yc,tx,ty)
        setidentity(composite_matrix)
        #translate(tx,ty)
        #xc=matrix[0][0]
        #yc=matrix[1][0]
        #draw(xc,yc)
        
        ch=input("if wanna rotate press 1:")
	if ch==1:
	  #setidentity(composite_matrix)	 	       
          theta=float(input("Enter theta: "))
	  refpoint_x=input("Enter reference point_x: ")
	  refpoint_y=input("Enter reference point_y: ")
	  rotate(theta,refpoint_x,refpoint_y)
	  glBegin(GL_POINTS)
	  for j in range(6):
	    xc=xc+tx
	    yc=yc+ty
	    for i in range(360) :
                angle=float(i*float(3.14/180))
                x=xc+rx*math.cos(angle)
                y=yc+ry*math.sin(angle)
                matrix[0][0]=x
		matrix[1][0]=y
		matrix[2][0]=1
		matrix_multiply(composite_matrix,matrix)
		x=matrix[0][0]
		y=matrix[1][0]
                glVertex2f(x,y)
                #angle+=n   
          glEnd()
          glFlush()
        check=int(input("Enter 0 to exit: "))
	if check==0:
		time.sleep(1)
		sys.exit()  
        
	
def Display():
  glColor3f(1.0,0.0,0.0)
  glPointSize(3.0)
  drawaxis()
  glColor3f(0.8,0.5,0.0)
  drawellipse()
                                      
def main():
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
        glutInitWindowPosition(40,40)
        glutInitWindowSize(400,400)
        glutCreateWindow("polar ellipse")
        glutDisplayFunc(Display)
        init()
        glutMainLoop()
main()        

"""
enter the centre of ellipse:  -100,-200
enter the major and minor axis: 300,100
enter tx,ty:30,30
if wanna rotate press 1:1
Enter theta: 75
Enter reference point_x: 50
Enter reference point_y: 50
Enter 0 to exit: 0
"""
