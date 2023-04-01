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

glClearColor(0.6, 1, 1, 1)

pipeline = es.SimpleTransformShaderProgram()
controller.pipeline = pipeline
glUseProgram(pipeline.shaderProgram)

def createSpecificTriangle(x1,y1,z1,x2,y2,z2,x3,y3,z3,r1, g1, b1,r2, g2, b2,r3, g3, b3):
  
    vertices = [
        x1, y1, z1,  r1, g1, b1,
        x2, y2, z2,  r2, g2, b2,
        x3,  y3, z3,  r3, g3, b3]

    indices = [0, 1, 2]

    return Shape(vertices, indices)

def createSpecificQuad(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,r1, g1, b1,r2,g2,b2,r3,g3,b3,r4,g4,b4):

    # Defining locations and colors for each vertex of the shape    
    vertices = [
    #   positions        colors
        x1, y1, z1,  r1, g1, b1,
        x2, y2, z2,  r2, g2, b2,
        x3, y3, z3,  r3, g3, b3,
        x4, y4, z4,  r4, g4, b4]

    # Defining connections among vertices
    # We have a triangle every 3 indices specified
    indices = [
         0, 1, 2,
         2, 3, 0]

    return Shape(vertices, indices)


alaDerSup = HighLevelGPUShape(pipeline, createSpecificTriangle(0.0,0.0,0.0,  0.321,0.367,0.0,  0.3,0.0,0.0,  1, 0.3, 0.1,  1, 0.6, 0.0,  1, 0.4, 0.1))

alaDerInf = HighLevelGPUShape(pipeline, createSpecificTriangle(0.0,0.0,0.0,  0.193,-0.35,0.0,  0.3,0.0,0.0,  1, 0.3, 0.1,  1, 0.6, 0.0,  1, 0.4, 0.1))

alaIzqSup = HighLevelGPUShape(pipeline, createSpecificTriangle(0.0,0.0,0.0,  -0.321,0.367,0.0,  -0.3,0.0,0.0,  1, 0.3, 0.1,  1, 0.6, 0.0,  1, 0.4, 0.1))

alaIzqInf = HighLevelGPUShape(pipeline, createSpecificTriangle(0.0,0.0,0.0,  -0.193,-0.35,0.0,  -0.3,0.0,0.0,  1, 0.3, 0.1,  1, 0.6, 0.0,  1, 0.4, 0.1))

cuerpo = HighLevelGPUShape(pipeline, createSpecificQuad(-0.05,0.2,0.0,  0.05,0.2,0.0,  0.05,-0.2,0.0,  -0.05,-0.2,0.0,  0.6,0.3,0.0,  0.6,0.3,0.0,  0.6,0.3,0.0,  0.6,0.3,0.0))

antenaIzq= HighLevelGPUShape(pipeline,createSpecificQuad(-0.095,0.255,0.0,  -0.085,0.265,0.0,  -0.04,0.2,0.0,  -0.05,0.19,0.0,  0.6,0.3,0.0,  0.6,0.3,0.0,  0.6,0.3,0.0,  0.6,0.3,0.0))

antenaDer= HighLevelGPUShape(pipeline,createSpecificQuad(0.095,0.255,0.0,  0.085,0.265,0.0,  0.04,0.2,0.0,  0.05,0.19,0.0,  0.6,0.3,0.0,  0.6,0.3,0.0,  0.6,0.3,0.0,  0.6,0.3,0.0))


def drawTriangle(controller: Controller, triangle):
    triangle.draw(controller.pipeline)

def drawQuad(controller: Controller, quad):
    quad.draw(controller.pipeline)
    
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
    alaDerSup.draw(controller.pipeline)
    
    drawTriangle(controller,alaDerInf)
    drawTriangle(controller,alaIzqInf)
    drawTriangle(controller,alaIzqSup)
    drawQuad(controller,cuerpo)
    drawQuad(controller,antenaIzq)  
    drawQuad(controller,antenaDer)  
        

# Try to call this function 60 times per second
pyglet.clock.schedule(update, controller)
# Se ejecuta la aplicación
pyglet.app.run()