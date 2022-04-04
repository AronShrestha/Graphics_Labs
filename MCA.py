
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from base import Drawing


class MCA(Drawing):
    def display_function(self):
        xc,yc=180.0,180.0
        r = 89.0
        x=0
        y=r
        P= 5/4 -r

                
        
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_POINTS)
    
        k = 0
        while x <= y:
            print(k)
            k=k+1

            if P < 0:
                x = x + 1 
                glVertex2d(round(x+xc),round(y+yc))
                P = P + 2*x + 1
            
            else:
                x = x + 1
                y = y -1
                glVertex2d(round(x + xc),round(y + yc))
                P = P + 2*x -2*y +1
            print('k-{} Pk-{} (x,y)-({},{}) '.format(k,P,x,y))
            glVertex2d(round(x+ xc),round(-y + yc))
            glVertex2d(round(-x + xc),round(y + yc))
            glVertex2d(round(-x + xc),round(-y + yc))
            glVertex2d(round(y + yc),round(x + xc))
            glVertex2d(round(y+ yc),round(-x + xc))
            glVertex2d(round(-y + yc),round(x + xc))
            glVertex2d(round(-y + yc),round(-x + xc))
        glEnd()
        glFlush()


circle = MCA()
circle.Driver()