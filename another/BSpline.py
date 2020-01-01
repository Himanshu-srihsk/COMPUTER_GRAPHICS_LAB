from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from time import *
t=[0 for i in range(30)]
def Init():
	glClearColor(0.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glPointSize(3.0)
	gluOrtho2D(0,600,0,600)
def setPixel(x,y):
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glFlush()
def read_controlPoint():
	global Px,Py,no_controlPoint,k
	no_controlPoint=input("Enter the no. of control point")
	k=input("Enter order of curve")
	Px=[0 for x in range(no_controlPoint)]
	Py=[0 for y in range(no_controlPoint)]
	for i in range(no_controlPoint):
		Px[i]=input("Enter the controlPoint_x")
		Py[i]=input("Enter the controlPoint_y")
		setPixel(Px[i],Py[i])
def calc_knot_value():
	n=no_controlPoint-1
	for i in range(n+k+1):
		if i<k:
			t[i]=0
		elif k<=i<=n:
			t[i]=i-k+1
		elif i>n:
			t[i]=n-k+2
def Bspline(i,k,u):
	result=0
	if k==1:
		if (t[i]<u and u<t[i+1]):
			return 1
		else:
			return 0
	if (t[i+k-1]-t[i])!=0:
		result+=float(((u-t[i])*Bspline(i,k-1,u))/(t[i+k-1]-t[i]))
	if (t[i+k]-t[i+1])!=0:
		result+=float(((t[i+k]-u)*Bspline(i+1,k-1,u))/(t[i+k]-t[i+1]))
	return result
def Bsplinefun():
	n=no_controlPoint-1
	calc_knot_value()
	u=0.0
	while u<=n-k+2:
		x=0.0
		y=0.0
		for i in range(no_controlPoint):
			x+=Bspline(i,k,u)*Px[i]
			y+=Bspline(i,k,u)*Py[i]
		setPixel(x,y)
		u+=0.005
def draw_Bspline_Curve():
	while True:
		read_controlPoint()
		Bsplinefun()
		print("Enter any decimal to continue")
		check=int(input("Enter 0 to exit"))
		if check==0:
			sleep(5)
			sys.exit()
		else:
			pass
def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	draw_Bspline_Curve()
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE| GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Bspline_Curve")
	glutDisplayFunc(Display)
	Init()
	glutMainLoop()
main()

