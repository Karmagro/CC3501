import pyglet
from pyglet.gl import *
import numpy as np
import math

window = pyglet.window.Window(640, 480, visible=True)

# Shader source code for the vertex and fragment shaders
vertex_shader_source = """
#version 330
in vec2 position;
void main() {
    gl_Position = vec4(position, 0.0, 1.0);
}
"""

fragment_shader_source = """
#version 330
out vec4 out_color;
void main() {
    out_color = vec4(1.0, 0.0, 0.0, 1.0);
}
"""

# Create the shader program
shader_program = glCreateProgram()

# Create the vertex shader, compile it, and attach it to the shader program
vertex_shader = glCreateShader(GL_VERTEX_SHADER)
glShaderSource(vertex_shader, vertex_shader_source)
glCompileShader(vertex_shader)
glAttachShader(shader_program, vertex_shader)

# Create the fragment shader, compile it, and attach it to the shader program
fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
glShaderSource(fragment_shader, fragment_shader_source)
glCompileShader(fragment_shader)
glAttachShader(shader_program, fragment_shader)

# Link the shader program
glLinkProgram(shader_program)

# Create a vertex buffer for the circle
num_segments = 64
vertices = []
for i in range(num_segments):
    angle = 2 * math.pi * i / num_segments
    x = math.cos(angle)
    y = math.sin(angle)
    vertices += [x, y]
vbo = (GLfloat * len(vertices))(*vertices)
vbo_size = len(vertices) * 4

# Create a vertex array object for the circle
vao = GLuint(0)
glGenVertexArrays(1, vao)
glBindVertexArray(vao)
vbo_handle = GLuint(0)
glGenBuffers(1, vbo_handle)
glBindBuffer(GL_ARRAY_BUFFER, vbo_handle)
glBufferData(GL_ARRAY_BUFFER, vbo_size, vbo, GL_STATIC_DRAW)
glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)
glEnableVertexAttribArray(0)

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)

    # Use the shader program to draw the circle
    glUseProgram(shader_program)
    glBindVertexArray(vao)
    glDrawArrays(GL_TRIANGLE_FAN, 0, num_segments)

pyglet.app.run()
