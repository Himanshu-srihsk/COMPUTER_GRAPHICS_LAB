from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys
import math


def ROUND(a):
    return int(a + 0.5)

def init():
  glClearColor(1.0,1.0,1.0,1.0)
  glMatrixMode(GL_PROJECTION)
  
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
   
def draw(xc,yc): 
        angle=0
        x=rx
        y=0
        n=float(1)/float(rx)
        while angle<=2*3.14 :
                x=xc+rx*math.cos(angle)
                y=yc+ry*math.sin(angle)
                setPixel(x,y)
                angle+=n    
                




                  
def drawellipse():
        global xc,yc,rx,ry
        xc,yc=input("enter the centre of ellipse:  ")
        rx,ry=input("enter the major and minor axis: ")
        draw(xc,yc)
        print("do u want to translate y/n")
        ch=raw_input()
        if ch=='y':
                tx,ty=input("trans  ")
                for i in range(1,6):
                  translation(tx,ty) 
        elif ch=='s':
                refx,refy=input("reference point  ")
                scale(sx,sy,refx,refy)        
        else:
                exit()    
 
              
def translation(tx,ty):
        matrix1=[[1,0,tx],[0,1,ty],[0,0,1]]
        matrix2=[[0 for i in range(1)] for j in range(3)]
        matrix2[0][0]=xc
        matrix2[1][0]=yc
        matrix2[2][0]=1
        matrix3=[[0 for i in range(1)] for j in range(3)]
        for i in range(len(matrix1)):
                for j in range(len(matrix2[0])):
                        for k in range(len(matrix1)):
                                matrix3[i][j]+=matrix1[i][k]*matrix2[k][j]
                                

        x1=matrix3[0][0]
        y1=matrix3[1][0]
        draw(x1,y1)



def scale(sx,sy,refpoint_x,refpoint_y):
        #refpoint_x=input("enter pivot_x point")
        #refpoint_y=input("enter pivot_y point")
        #sx=input("enter sx")
        #sy=input("enter sy")
	tx=refpoint_x - 0
	ty=refpoint_y - 0
	translation(-tx,-ty)
	#m=[[0 for x in range(3)] for y in range(3)]
	#matrix_set_identity(m)
	#m[0][0]=sx
	#m[1][1]=sy
	matrix1=[[1,0,sx],[0,1,sy],[0,0,1]]
	matrix_multiply(matrix1,composite_matrix)
	translate(tx,ty)
	
def Display():
  glClear(GL_COLOR_BUFFER_BIT)
  glColor3f(0.0,0.0,0.0)
  glPointSize(3.0)
  drawaxis()
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

