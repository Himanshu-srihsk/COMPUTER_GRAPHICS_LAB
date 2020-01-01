from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def init(w,h):
    glClearColor(0.0,1.0,0.0,0.0)
    glColor3f(1.0,0.0,0.0)
    glMatrixMode(GL_PROJECTION)
    glPointSize(2.0)
    glLoadIdentity()
    gluOrtho2D(-w,w,-h,h)




def calc(x,y):

    result=[]
    for i in range(len(x)):
        row=[]
        for j in range(len(y[0])):
            sum =0
            for k in range(len(y)):
                sum += x[i][k] * y[k][j]
            row.append(sum)
        result.append(row)
    return result






def bezier():

    m=[[-1,3,-3,1],
    [3, -6, 3, 0],
    [-3, 3, 0, 0],
    [1, 0, 0, 0]]

    calcx=calc(m,px)
    calcy=calc(m,py)





    u = 0.0
    k=[]
    while u <= 1.0:
        um=[[u*u*u ,u*u,u,1]]
        x=calc(um,calcx)
        y=calc(um, calcy)
        glVertex2f(x[0][0],y[0][0])
        u += 0.0005






def inputall():

    global px, py
    n = int(input("Enter no of control points: "))
    px = []
    py = []
    for i in range(n):
        px.append([input("Enter control point_x: ")])
        py.append([input("Enter control point_y: ")])




def display():
    glBegin(GL_POINTS)
    bezier()
    glEnd()
    glFlush()






def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    global w, h
    h = input("enter the height")
    w = input("enter the width")
    glutInitWindowSize(w,h)
    glutInitWindowPosition(50,50)
    glutCreateWindow("bezier curve")
    inputall()
    glutDisplayFunc(display)
    init(w,h)
    glutMainLoop()

main()
