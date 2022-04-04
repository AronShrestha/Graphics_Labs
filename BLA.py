from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from base import Drawing

class BLA_Line(Drawing):
    def display_function(self):
        x1,x2,y1,y2 = 120.0,300.0,50.0,350.0
        x,y=x1,y1
        dx=x2-x1
        dy=y2-y1
        if abs(dy) >abs(dx):
            P= 2*dy -dx
 
            glClear(GL_COLOR_BUFFER_BIT)
            glBegin(GL_POINTS)
            glVertex2d(x,y)

            for i in range(int(abs(dx)+1)):
                
                if P <0:
                    x = x+1.0 
                    glVertex2d(round(x),round(y))
                    P =  P +2*dy
                else:
                    x = x+1.0 
                    y= y + 1.0
                    glVertex2d(round(x),round(y))
                    P =  P +2*dy -2*dx
                print('i {} p {} (x,y) {}, {}'.format(i,P,x,y))     
            
        else:
                P = 2*dx-dy
                for i in range(int(abs(dy)+1)):
                    
                    if P <0:
                        y = y+1.0 
                        glVertex2d(round(x),round(y))
                        P =  P +2*dx
                    else:
                        x = x+1.0 
                        y= y + 1.0
                        glVertex2d(round(x),round(y))
                        P =  P +2*dx -2*dy
                    print('i {} p {} (x,y) {}, {}'.format(i,P,x,y))     
            



        glEnd()
        glFlush()



BLA = BLA_Line()
BLA.Driver()


