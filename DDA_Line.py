
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from base import Drawing
class DDA_Line(Drawing):
    def display_function(self):
        x1,x2,y1,y2 = 120.0,300.0,50.0,350.0
        x,y=x1,y1
        dx=x2-x1
        dy=y2-y1
        if abs(dx) > abs(dy):
            step_size = abs(dx)
        else:
            step_size = abs(dy)
        xinc = dx / step_size
        yinc = dy / step_size


        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_POINTS)
        glVertex2d(x,y)
        for i in range(int(step_size)+1):
            x = x + xinc
            y = y + yinc
            glVertex2d(round(x),round(y))


        glEnd()
        glFlush()

dda_line = DDA_Line()
dda_line.Driver()



