import pyglet
from OpenGL.GL import *

from math import cos, sin
from random import random,seed

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

    def __init__(self, width, height, title="Tarea 1: Mariposa que se mueve y aletea", resizable=True):
        super().__init__(width, height, title,resizable)
        self.total_time = 0.0
        self.fillPolygon = True
        self.pipeline = None
        self.repeats = 0
        self.mariposaSpeedX = 0
        self.mariposaSpeedY = 0
        self.mariposaPosX = 0
        self.mariposaPosY = 0
        self.mariposaPosZ = 0
        self.enjambreSpeed= 1

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

#cuerpo = HighLevelGPUShape(pipeline, createSpecificQuad(-0.05,0.2,0.0,  0.05,0.2,0.0,  0.05,-0.2,0.0,  -0.05,-0.2,0.0,  0.6,0.3,0.0,  0.6,0.3,0.0,  0.6,0.3,0.0,  0.6,0.3,0.0))

cuerpo = HighLevelGPUShape(pipeline, createSpecificQuad(-0.03,0.2,0.0,  0.03,0.2,0.0,  0.03,-0.25,0.0,  -0.03,-0.25,0.0,  0,0,0,  0,0,0,  0,0,0, 0,0,0))

antenaIzq= HighLevelGPUShape(pipeline,createSpecificQuad(-0.095,0.275,0.0,  -0.085,0.285,0.0,  -0.02,0.2,0.0,  -0.03,0.19,0.0,  0,0,0,  0,0,0,  0,0,0, 0,0,0))

antenaDer= HighLevelGPUShape(pipeline,createSpecificQuad(0.095,0.275,0.0,  0.085,0.285,0.0,  0.02,0.2,0.0,  0.03,0.19,0.0,  0,0,0,  0,0,0,  0,0,0, 0,0,0))

ojoIzq= HighLevelGPUShape(pipeline,createSpecificQuad(-0.02,0.19,0.0,  -0.01,0.19,0.0,  -0.01,0.16,0.0,  -0.02,0.16,0.0,  1,0.1,0.7,  1,0.1,0.7,  1,0.1,0.7, 1,0.1,0.7))

ojoDer= HighLevelGPUShape(pipeline,createSpecificQuad(0.01,0.19,0.0, 0.02,0.19,0.0,    0.02,0.16,0.0,  0.01,0.16,0.0,  1,0.1,0.7,  1,0.1,0.7,  1,0.1,0.7, 1,0.1,0.7))

mariposa= [alaDerSup,alaDerInf,alaIzqSup,alaIzqInf,cuerpo,antenaDer,antenaIzq,ojoIzq,ojoDer]

def draw_moving_mariposa(controller: Controller):

    for parte in mariposa:
        if parte==alaDerSup or parte==alaDerInf or parte==alaIzqInf or parte==alaIzqSup:
            parte._transform = tr.matmul([tr.translate(controller.mariposaPosX, controller.mariposaPosY, 0),
                                        tr.uniformScale(0.3+controller.total_time%0.7)])
        else:
            parte._transform = tr.matmul([tr.translate(controller.mariposaPosX, controller.mariposaPosY, 0),
                                        tr.uniformScale(1)])
        parte.draw(controller.pipeline)


def draw_enjambre(controller: Controller):
    i=0
    rutina = [[0.4*cos(controller.total_time),-0.4*sin(controller.total_time),0.0],
              [-0.9*cos(controller.total_time),0.9*sin(controller.total_time),0.0],
              [0.5*cos(controller.total_time),0.5*sin(controller.total_time),0.0],
              [-0.7*cos(controller.total_time),-0.7*sin(controller.total_time),0.0],
              [1*cos(controller.total_time),-1*sin(controller.total_time),0.0]]
    while i<5:
        for parte in mariposa:
                seed(i)
                if parte==alaDerSup or parte==alaDerInf or parte==alaIzqInf or parte==alaIzqSup:
                    parte._transform = tr.identity()  # Make the transform neutral again
                    parte.rotation = tr.rotationZ(controller.total_time*random()*2)
                    parte.translation = tr.translate(rutina[i][0],rutina[i][1],rutina[i][2])
                    parte.scale = tr.uniformScale(0.1 + controller.total_time%0.2)
                    parte.draw(controller.pipeline)

                else:
                    parte._transform = tr.identity()  # Make the transform neutral again
                    parte.rotation = tr.rotationZ(controller.total_time*random()*2)
                    parte.translation = tr.translate(rutina[i][0],rutina[i][1],rutina[i][2])
                    parte.scale = tr.uniformScale(0.3)
                    parte.draw(controller.pipeline)            
        i+=1

@controller.event
def on_key_press(symbol, modifiers):
    controller.mariposaSpeedX = 0
    controller.mariposaSpeedY = 0
    

    if symbol == pyglet.window.key.SPACE:
        controller.fillPolygon = not controller.fillPolygon
    elif symbol == pyglet.window.key.ESCAPE:
        controller.close()
    
    elif symbol == pyglet.window.key.LEFT:
        controller.mariposaSpeedX -= 1

    elif symbol == pyglet.window.key.RIGHT:
        controller.mariposaSpeedX += 1

    elif symbol == pyglet.window.key.DOWN:
        controller.mariposaSpeedY -= 1

    elif symbol == pyglet.window.key.UP:
        controller.mariposaSpeedY += 1

@controller.event
def on_key_release(symbol, modifiers):
    if symbol == pyglet.window.key.LEFT:
        controller.mariposaSpeedX = 0

    elif symbol == pyglet.window.key.RIGHT:
        controller.mariposaSpeedX = 0
    
    elif symbol == pyglet.window.key.DOWN:
        controller.mariposaSpeedY = 0

    elif symbol == pyglet.window.key.UP:
        controller.mariposaSpeedY = 0
    
def update(dt, controller):
    controller.total_time += dt
    controller.mariposaPosX += controller.mariposaSpeedX * dt
    controller.mariposaPosY += controller.mariposaSpeedY * dt


@controller.event
def on_draw():
    controller.clear()

    # Si el controller está en modo fillPolygon, dibuja polígonos. Si no, líneas.
    if controller.fillPolygon:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    else:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    
    # Dibuja las figuras
    draw_moving_mariposa(controller)
    draw_enjambre(controller)    

# Try to call this function 60 times per second
pyglet.clock.schedule(update, controller)
# Se ejecuta la aplicación
pyglet.app.run()