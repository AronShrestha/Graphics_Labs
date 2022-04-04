from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
from base import Drawing


class PieChart(Drawing):
    def display_function(self):


        xc,yc=200.0,200.0
        r = 90.0
        x=0
        y=r
        P= 5/4 -r
        datas = [120,200,260,300,190]
        total = 0
        for i in range(len(datas)):
            total += datas[i]

        print(total)           
        glColor3f(0.2,0.5,0.4) #RGB    
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_POINTS)
    
        k = 0
        while x <= y:
        
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
            # print('k-{} Pk-{} (x,y)-({},{}) '.format(k,P,x,y))
            glVertex2d(round(x+ xc),round(-y + yc))
            glVertex2d(round(-x + xc),round(y + yc))
            glVertex2d(round(-x + xc),round(-y + yc))
            glVertex2d(round(y + yc),round(x + xc))
            glVertex2d(round(y+ yc),round(-x + xc))
            glVertex2d(round(-y + yc),round(x + xc))
            glVertex2d(round(-y + yc),round(-x + xc))
        
        glEnd()
        self.display(xc,yc,r,datas,total)
        glFlush()
        


    def display(self,xc,yc,r,datas,total):
        angle=0
        glBegin(GL_LINES)
        glColor3d(1,0,0)
        for i in range(len(datas)):
            angle = (2*math.pi*datas[i]/total +angle)
            x =  xc + r*math.cos(angle)
            y =  yc + r*math.sin(angle)
            glVertex2d(x,y)
            glVertex2d(xc,yc)
        glEnd()

    
 
    
  
pie_chart =  PieChart()
pie_chart.Driver()


  







