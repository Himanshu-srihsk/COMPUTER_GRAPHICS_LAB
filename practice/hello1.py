import sys
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
x1,y1=[],[]
for i in range(3):
	x1+=[int(input("enter x"+str(i+1)+" "))]
	y1+=[int(input("enter y"+str(i+1)+" "))]
def init():
	glClearColor(1.0,1.0,1.0,1.0)
        gluOrtho2D(-100.0,100.0,-100.0,100.0)
def draw(x,y,c):
	if c>5:
		return
	c+=1
	x2,y2=[(x[0]+x[1])/2,(x[2]+x[1])/2,(x[0]+x[2])/2],[(y[0]+y[1])/2,(y[1]+y[2])/2,(y[0]+y[2])/2]
	for i in range(3):
		glVertex2f(round(x2[i]),round(y2[i]))
		glVertex2f(round(x2[(i+1)%3]),round(y2[(i+1)%3]))
		draw([x2[i],x2[(i+1)%3],x[(i+1)%3]],[y2[i],y2[(i+1)%3],y[(i+1)%3]],c)
def dda(x1,y1,x2,y2):
	dx=x2-x1
	dy=y2-y1	
	step=max(abs(dx),abs(dy))
	xinc=float(dx/step)
	yinc=float(dy/step)
	for i in range(int(step)+1):
		glBegin(GL_POINTS)
		glVertex2f(round(x1),round(y1))
		glEnd()
		glFlush()
		x1+=xinc
		y1+=yinc	
def bres():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glColor3f(0.0,0.0,0.0)
        glPointSize(2.0)
        
	x,y=x1,y1
	for i in range(3):
		dda(round(x1[i]),round(y1[i]),round(x1[(i+1)%3]),round(y1[(i+1)%3]))
	glBegin(GL_LINES)
	draw(x,y,1)
	glEnd()
	glFlush()
	
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowPosition(50,50)
	glutInitWindowSize(400,400)
	glutCreateWindow("Function Plotter")
	init()
	glutDisplayFunc(bres)	
	glutMainLoop()
main()
