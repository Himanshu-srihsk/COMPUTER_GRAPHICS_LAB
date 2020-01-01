from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from datetime import *
from time import *
import sys
import signal

matrix=[[0 for x in range(1)] for y in range(3)]   
composite_matrix=[[0 for x in range(3)] for y in range(3)]  
xcenter,ycenter
radius=200
hradius=80
mradius=100
sradius=140


def ROUND(a):
	return int(a+0.5)

def signal_handler(sig, frame):
        print('You pressed Ctrl+C! to terminate program')
        sys.exit(0)

def init():
	glClearColor(0.0,0.0,0.0,0.0)
	glPointSize(4.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-window_x/2,window_x/2,-window_y/2,window_y/2)

def setPixel(x,y):
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glFlush()

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


def draw_circle(xcenter,ycenter,radius):
	glColor(1.0,0.0,0.0)
	theta=0
	while theta <=360:
		angle=(3.14*theta)/180
		x=xcenter+radius*cos(angle)
		y=ycenter+radius*sin(angle)
		setPixel(x,y)
		theta+=0.5

def glut_print( x,  y,  font,  text, r,  g , b , a):
    glRasterPos2f(x,y)
    for ch in text :
        glutBitmapCharacter( font , ctypes.c_int( ord(ch) ) )

        
def Draw():
	glColor3f(0,1,1)
	glut_print( xcenter+dradius*cos(-60*3.14/180),ycenter+dradius*sin(-60*3.14/180) , GLUT_BITMAP_9_BY_15 , "5" , 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(xcenter+dradius*cos(-30*3.14/180),ycenter+dradius*sin(-30*3.14/180), GLUT_BITMAP_9_BY_15 , "4" , 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(xcenter+dradius,ycenter , GLUT_BITMAP_9_BY_15 , "3" , 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(xcenter+dradius*cos(30*3.14/180),ycenter+dradius*sin(30*3.14/180) , GLUT_BITMAP_9_BY_15 , "2" , 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(xcenter+dradius*cos(60*3.14/180),ycenter+dradius*sin(60*3.14/180),GLUT_BITMAP_9_BY_15 , "1" , 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(xcenter,ycenter+dradius, GLUT_BITMAP_9_BY_15 , "12" , 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(xcenter+dradius*cos(120*3.14/180),ycenter+dradius*sin(120*3.14/180),GLUT_BITMAP_9_BY_15 , "11" , 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(xcenter+dradius*cos(150*3.14/180),ycenter+dradius*sin(150*3.14/180), GLUT_BITMAP_9_BY_15 , "10" , 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(xcenter-dradius,ycenter , GLUT_BITMAP_9_BY_15 , "9" , 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(xcenter+dradius*cos(210*3.14/180),ycenter+dradius*sin(210*3.14/180) , GLUT_BITMAP_9_BY_15 , "8" , 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(xcenter+dradius*cos(240*3.14/180),ycenter+dradius*sin(240*3.14/180), GLUT_BITMAP_9_BY_15 , "7" , 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(xcenter,ycenter-dradius, GLUT_BITMAP_9_BY_15 , "6" , 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print( -35 ,-250, GLUT_BITMAP_9_BY_15 , ":" , 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print( 0 ,-250, GLUT_BITMAP_9_BY_15 , ":" , 1.0 , 1.0 , 1.0 , 1.0 )
	# draw my scene ......
	#glFlush()

def matrix_set_identity(m):
	for i in range(3):
		for j in range(3):
			if i==j:
				m[i][j]=1


def matrix_multiply(matrix_a,matrix_b):
	temp_matrix=[[0 for x in range(len(matrix_b[0]))] for y in range(len(matrix_a))]
	for i in range(len(matrix_a)):
		for j in range(len(matrix_b[0])):
			for k in range(len(matrix_a)):
				temp_matrix[i][j]+=matrix_a[i][k]*matrix_b[k][j]

	for i in range(len(matrix_b)):
		for j in range(len(matrix_b[0])):
			matrix_b[i][j]=temp_matrix[i][j]

def translate(tx,ty):
	m1=[[0 for x in range(3)] for y in range(3)]
	matrix_set_identity(m1)
	m1[0][2]=tx
	m1[1][2]=ty
	matrix_multiply(m1,composite_matrix)

def rotate(theta,refpoint_x,refpoint_y):
	tx=refpoint_x - 0
	ty=refpoint_y - 0
	translate(-tx,-ty)
	m=[[0 for x in range(3)] for y in range(3)]
	matrix_set_identity(m)
	theta=3.14159*(theta/180)
	m[0][0]=cos(theta)
	m[0][1]=sin(theta)
	m[1][0]=-sin(theta)
	m[1][1]=cos(theta)
	matrix_multiply(m,composite_matrix)
	translate(tx,ty)

def get_time():
	global hr,mint,sec
	currentT=datetime.now()
	hr=currentT.hour
	if hr > 12:
		hr=hr- 12
	mint=currentT.minute
	sec=currentT.second
	
def clock():
	get_time()
	matrix_set_identity(composite_matrix)
	sx=xcenter+sradius*cos((90-sec*6)*3.14/180) 
	sy=ycenter+sradius*sin((90-sec*6)*3.14/180)
	mx=xcenter+mradius*cos((90-mint*6)*3.14/180) 
	my=ycenter+mradius*sin((90-mint*6)*3.14/180)
	hx=xcenter+hradius*cos((90-hr*30)*3.14/180)
	hy=ycenter+hradius*sin((90-hr*30)*3.14/180)
	glColor(1.0,1.0,1.0)
	lineDDA(xcenter,ycenter,sx,sy)
	glColor(1.0,1.0,0.0)
	lineDDA(xcenter,ycenter,mx,my)
	glColor(1.0,0.0,1.0)
	lineDDA(xcenter,ycenter,hx,hy)
	s=sec
	m=mint
	h=hr
	while True:
		get_time()
		if sec ==0:
			s1=60
			mi=mint-1
		else:
			s1=sec-1
			mi=mint
		if mint==0:
			h1=hr-1
		else:
			h1=hr
		glColor3f(0,0,0)
		glut_print(10 ,-250, GLUT_BITMAP_9_BY_15 ,str(s1), 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(1,1,1)
		glut_print( 10 ,-250, GLUT_BITMAP_9_BY_15 , str(sec) , 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(0,0,0)
		glut_print( -20 ,-250, GLUT_BITMAP_9_BY_15 , str(mi) , 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(1,1,1)
		glut_print( -20 ,-250, GLUT_BITMAP_9_BY_15 , str(mint) , 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(0,0,0)
		glut_print( -50 ,-250, GLUT_BITMAP_9_BY_15 , str(h1) , 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(1,1,1)
		glut_print( -50 ,-250, GLUT_BITMAP_9_BY_15 , str(hr) , 1.0 , 1.0 , 1.0 , 1.0 )
		sleep(1)
		glColor(0.0,0.0,0.0)
		lineDDA(xcenter,ycenter,sx,sy)
		matrix[0][0]=sx
		matrix[1][0]=sy
		matrix[2][0]=1
		rotate(6,xcenter,ycenter)
		matrix_multiply(composite_matrix,matrix)
		sx=matrix[0][0]
		sy=matrix[1][0]
		glColor(1.0,1.0,1.0)
		lineDDA(xcenter,ycenter,sx,sy)
		s=s+1
		if s==60:
			glColor(0.0,0.0,0.0)
			lineDDA(xcenter,ycenter,mx,my)
			matrix[0][0]=mx
			matrix[1][0]=my
			matrix[2][0]=1
			rotate(6,xcenter,ycenter)
			matrix_multiply(composite_matrix,matrix)
			mx=matrix[0][0]
			my=matrix[1][0]
			glColor(1.0,1.0,0.0)
			lineDDA(xcenter,ycenter,mx,my)
			m+=1
			if m==60:
				glColor(0.0,0.0,0.0)
				lineDDA(xcenter,0,hx,hy)
				matrix[0][0]=hx
				matrix[1][0]=hy
				matrix[2][0]=1
				rotate(30,xcenter,ycenter)
				matrix_multiply(composite_matrix,matrix)
				mx=matrix[0][0]
				my=matrix[1][0]
				glColor(1.0,0.0,1.0)
				lineDDA(0,0,hx,hy)
		
		

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	draw_circle(xcenter,ycenter,radius)
	Draw()
	glut_print(-50 ,-280, GLUT_BITMAP_9_BY_15 ,str(datetime.now().day), 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(-30 ,-280, GLUT_BITMAP_9_BY_15 ,"-", 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(-20,-280, GLUT_BITMAP_9_BY_15 ,str(datetime.now().month), 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(0 ,-280, GLUT_BITMAP_9_BY_15 ,"-", 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(10 ,-280, GLUT_BITMAP_9_BY_15 ,str(datetime.now().year), 1.0 , 1.0 , 1.0 , 1.0 )
	clock()
	

def main():
	signal.signal(signal.SIGINT, signal_handler)
	readinput()
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	window_x=int(input("Enter length of window in x-direction: "))
	window_y=int(input("Enter length of window in y-direction: "))
	xcenter=input("Enter xcenter: ")
	ycenter=input("Enter ycenter: ")
	glutInitWindowSize(window_x,window_y)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Clock")
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()
