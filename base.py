from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from abc import ABC, abstractmethod
 

class Drawing:

  
    def Driver(self):
        self.setup()
    
    def myInit(self):
        

        glClearColor(1.0,1.0,0.0,1.0) #RGBA
        glColor3f(0.2,0.5,0.4) #RGB
        glPointSize(2.0)
        gluOrtho2D(0,500,0,500) #left ,right , bottom ,top

    def setup(self):
        glutInit()

        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

        glutInitWindowSize(500,500) #(height,width)
        glutInitWindowPosition(100,100) #(x pos,y pos)
        glutCreateWindow("Lab1")
        self.myInit()
        glutDisplayFunc(self.display_function)
        glutMainLoop()
    
    @abstractmethod
    def display_function(self):
        pass










