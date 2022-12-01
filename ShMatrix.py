'''Clase con funciones OpenGl, shaders y el calculo de la matriz clase'''

from OpenGL.GL.shaders import *
from OpenGL.GL import *
import glm

fragmentacion_sombreado = '''   #version 460
                                layout (location = 0) out vec4 fragColor;
                                uniform vec3 color;
                                in vec3 ourColor;
                                void main()
                                {
                                    fragColor = vec4(color, 1.0f);
                                }'''

vertices_sombreado = '''    #version 460
                            layout (location = 1) in vec3 vertexColor;
                            layout (location = 0) in vec3 position;
                            uniform mat4 amatrix;
                            out vec3 ourColor;
                            void main()
                            {
                                gl_Position = amatrix * vec4(position, 1.0f);
                                ourColor = vertexColor;
                            }'''

def calculateMatrix(Angulo_Rotacionb):
    i = glm.mat4(1)
    rotacion_principal = glm.rotate(i, glm.radians(Angulo_Rotacionb), glm.vec3(0, 1, 0))
    traslation = glm.translate(i, glm.vec3(0, 0, 0))
    Escala_inicial = glm.scale(i, glm.vec3(1, 1, 1))
    CamaraTotal = traslation * rotacion_principal * Escala_inicial

    VistalA = glm.lookAt(
        glm.vec3(0, 0, 15),
        glm.vec3(0, 1, 0),
        glm.vec3(0, 1, 0)
    )
    Proy_1 = glm.perspective(
        glm.radians(45),
        1600/1200,
        0.1,
        1000.0
    )

    amatrix = Proy_1 * VistalA * CamaraTotal

    glUniformMatrix4fv(glGetUniformLocation(compileProgram(compileShader(fragmentacion_sombreado , GL_FRAGMENT_SHADER),compileShader(vertices_sombreado, GL_VERTEX_SHADER)), 'amatrix'),1,GL_FALSE,glm.value_ptr(amatrix))