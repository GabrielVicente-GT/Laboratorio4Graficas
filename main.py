#Gabriel Alejandro Vicente Lorenzo
#Laboratorio 4 20498

#Documento trabajado en clase
from CargandoObjeto import VerticesPrincipales
from OpenGL.GL.shaders import *
from OpenGL.GL import *
from ShMatrix import *
import pygame
import glm

#Variables Iniciales
anguloRotacion = 0
programaPrincipal = True
x,y = 0,-150
r,g,b = 255,0,0

#Se inicia pygame con un ancho y alto definido, ademas de llamar a Opengl como buf
pygame.init()
PantallaLab4 = pygame.display.set_mode((600,750),pygame.OPENGL | pygame.DOUBLEBUF)

#Shaders
glUseProgram(compileProgram(compileShader(fragmentacion_sombreado , GL_FRAGMENT_SHADER),compileShader(vertices_sombreado, GL_VERTEX_SHADER)))

#OBJ
CargandoObjeto = VerticesPrincipales('./OBJ/faraon.obj')

#Cargando valors de Objeto en arreglos
glBindVertexArray(glGenVertexArrays(2)[0])
glBindBuffer(GL_ARRAY_BUFFER, glGenBuffers(2)[0])
glBufferData(GL_ARRAY_BUFFER, CargandoObjeto.matriz_principal.nbytes, CargandoObjeto.matriz_principal, GL_STATIC_DRAW)

#Vertices del objeto
glBindVertexArray(glGenVertexArrays(1))

#Puntero de los atributos
glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE,8 * CargandoObjeto.matriz_principal.itemsize,ctypes.c_void_p(0))
glEnableVertexAttribArray(0)

#VColor de fondo
glClearColor(0,0,0, 1.0)

while programaPrincipal:

    #Limbia el OpenGl de un color definido
    glClear(GL_COLOR_BUFFER_BIT)

    #Viewpor asignado
    glViewport(x,y, 600,750)

    #Color variante
    color = glm.vec3(r,g,b)

    #Coloca la informacion de la ubicacion, y los tres vertices debido a que son triangulos
    glUniform3fv(glGetUniformLocation(compileProgram(compileShader(fragmentacion_sombreado , GL_FRAGMENT_SHADER),compileShader(vertices_sombreado, GL_VERTEX_SHADER)),'color'),1,glm.value_ptr(color))

    #Se dibujan los truangulos dependiendo de cada utpla de vertices
    glDrawArrays(GL_TRIANGLES, 0, len(CargandoObjeto.matriz_principal))
    
    #Se realizan los cambios de la matriz amatrix segun aumenta anguloRotacion
    calculateMatrix(anguloRotacion)
    #Timer que permite retrasar las iteraciones y rotacion
    pygame.time.wait(250)
    anguloRotacion-=10 
    #Actualizacion de pygame
    pygame.display.flip()

    #Por cada evento que lea pygame
    for event in pygame.event.get():
        #Si se presina la x se cierra el bucle
        if event.type == pygame.QUIT:
            programaPrincipal = False
        #Si se presiona una tecla
        if event.type == pygame.KEYDOWN:
            #Si la tecla ESC se presiona se termina el programa_principal
            if event.key == pygame.K_ESCAPE:
                programaPrincipal = False
                
            if event.key == pygame.K_UP:
                x,y = 0,0
                r,g,b = 255,0,0
            if event.key == pygame.K_LEFT:
                x,y = -100,-150
                r,g,b = 255,255,255
            if event.key == pygame.K_DOWN:
                x,y = 0,-200
                r,g,b = 0,255,0
            if event.key == pygame.K_RIGHT:
                x,y = 100,-150
                r,g,b = 0,0,255
            #Si las teclas WASD se presionan
            if event.key == pygame.K_w:
                x,y = 0,0
                r,g,b = 255,0,0
            if event.key == pygame.K_s:
                x,y = 0,-200
                r,g,b = 0,255,0
            if event.key == pygame.K_a:
                x,y = -100,-150
                r,g,b = 255,255,255
            if event.key == pygame.K_d:
                x,y = 100,-150
                r,g,b = 0,0,255
