#Bouncing Ball
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
#uncomment these lines later
#to see if there is any difference
#in the speed of the ball
#import psyco
#psyco.full()
# globals for animation, ball position
# and direction of motion
global anim, x, y ,dx, dy
x = -0.67
y = 0.34
dx = dy = 1
width = height = 500
axrng = 5.0
# No animation to start
anim = 0
def init():
   glClearColor(0.0, 0.0, 0.0, 1.0)
   glColor3ub(255, 0, 0)
   # Dimensions of the screen
   # Make axrng larger and see what happens!
   gluOrtho2D(-axrng, axrng, -axrng, axrng)
   
def idle():
  # We animate only if anim == 1, otherwise
  # the ball doesn't move
  if anim == 1:
     glutPostRedisplay()   
     
def bounce():
   global x, y, dx, dy
   glClear(GL_COLOR_BUFFER_BIT)
   # changes x and y
   x += 0.001*dx
   y += 0.001*dy
   # Keep the motion mathematics
   # Safe from harm and then
   # Move the ball location based on x and y
   glPushMatrix()
   glTranslate(x,y,0)
   glutSolidSphere(0.3, 50, 50)
   glPopMatrix()
   # Collision detection!
   # What happens here and why does this work?
   if x >= axrng or x <= -axrng:
     dx = -1*dx
   if y >= axrng or y <= -axrng:
     dy = -1*dy    
   glFlush()
   
def keyboard(key, x, y):
    # Allows us to quit by pressing 'Esc' or 'q'
    # We can animate by "a" and stop by "s"
    global anim
    if key == chr(27):
      sys.exit()
    if key == "a":
      # Notice we are making anim = 1
      # What does this mean? Look at the idle function
      anim = 1
    if key == "s":
      # STOP the ball!
      anim = 0
    if key == "q":
      sys.exit()  
     
def main():
   glutInit(sys.argv)
   glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
   glutInitWindowPosition(100,100)
   glutInitWindowSize(width,height)
   glutCreateWindow("PyBounce")
   glutDisplayFunc(bounce)
   glutKeyboardFunc(keyboard)
   glutIdleFunc(idle)
   init()
   glutMainLoop()
main()
   
