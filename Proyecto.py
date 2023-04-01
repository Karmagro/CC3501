import pyglet
from OpenGL.GL import *

from math import cos, sin

from grafica import basic_shapes as bs
from grafica import easy_shaders as es
from grafica import transformations as tr
from grafica.assets_path import getAssetPath
from shapes_utils import HighLevelGPUShape, createGPUShape
class Shape:
    def __init__(self, vertices, indices):
        self.vertices = vertices
        self.indices = indices

    def __str__(self):
        return "vertices: " + str(self.vertices) + "\n"\
            "indices: " + str(self.indices)

class Controller(pyglet.window.Window):

    def __init__(self, width, height, title="Auxiliar 2"):
        super().__init__(width, height, title)
        self.total_time = 0.0
        self.fillPolygon = True
        self.pipeline = None
        self.repeats = 0
        self.triangleSpeed = 0
        self.trianglePosX = 0

controller = Controller(width=1280, height=720)

glClearColor(0.15, 0.15, 0.15, 1.0)

pipeline = es.SimpleTransformShaderProgram()
controller.pipeline = pipeline
glUseProgram(pipeline.shaderProgram)

def createVerySpecificTriangle(x1,y1,z1,x2,y2,z2,x3,y3,z3,r1, g1, b1,r2, g2, b2,r3, g3, b3):
  
    vertices = [
        x1, y1, z1,  r1, g1, b1,
        x2, y2, z2,  r2, g2, b2,
        x3,  y3, z3,  r3, g3, b3]

    indices = [0, 1, 2]

    return Shape(vertices, indices)

alaDerSup = HighLevelGPUShape(pipeline, createVerySpecificTriangle(0.0,0.0,0.0,  0.47,0.356,0.0,  0.3,0.0,0.0,  0.990, 0.735, 0.139,  1, 0.3, 0.0,  0.990, 0.735, 0.139))

alaDerInf = HighLevelGPUShape(pipeline, createVerySpecificTriangle(0.0,0.0,0.0,  0.361,-0.325,0.0,  0.3,0.0,0.0,  0.15,0.0,0.2,  0.15,0.0,0.2,  0.15,0.0,0.2))

alaIzqSup = HighLevelGPUShape(pipeline, createVerySpecificTriangle(0.0,0.0,0.0,  -0.47,0.356,0.0,  -0.3,0.0,0.0,  0.15,0.0,0.2,  0.15,0.0,0.2,  0.15,0.0,0.2))

alaIzqInf = HighLevelGPUShape(pipeline, createVerySpecificTriangle(0.0,0.0,0.0,  -0.361,-0.325,0.0,  -0.3,0.0,0.0,  0.15,0.0,0.2,  0.15,0.0,0.2,  0.15,0.0,0.2))

def drawTriangle(controller: Controller, triangle):
    triangle.draw(controller.pipeline)

def update(dt, controller):
    controller.total_time += dt
    controller.trianglePosX += controller.triangleSpeed * dt


@controller.event
def on_draw():
    controller.clear()

    # Si el controller está en modo fillPolygon, dibuja polígonos. Si no, líneas.
    if controller.fillPolygon:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    
    # Dibuja las figuras
    drawTriangle(controller,alaDerSup)
    drawTriangle(controller,alaDerInf)
    drawTriangle(controller,alaIzqInf)
    drawTriangle(controller,alaIzqSup)

# Try to call this function 60 times per second
pyglet.clock.schedule(update, controller)
# Se ejecuta la aplicación
pyglet.app.run()