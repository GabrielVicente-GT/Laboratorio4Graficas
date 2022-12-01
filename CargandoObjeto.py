'''Clase combinatoria creada por renderer y referencia: https://www.youtube.com/watch?v=DKt4HRBqH1I&t=1180s'''

import numpy as matriz_externa

class VerticesPrincipales(object):
    
    def __init__(self, file):
        self.coordenadasTotales = []
        self.cordenadasVert = []
        self.coordenadasN = []
        self.coordenadasT = []
        self.BackUpVertices = []
        self.Caras = []

        with open(file, 'r') as f:
            line = f.readline()
            while line:
                values = line.split()
                if values[0] == 'f':

                    for value in values[1:]:
                        val = value.split('/')
                        for d in val:
                            if d == 'f':
                                continue
                            self.coordenadasTotales.append(int(d)-1)
                        self.Caras.append(int(val[0])-1)

                if values[0] == 'vn':
                    for d in values:
                        if d == 'vn':
                            continue
                        self.coordenadasN.append(float(d))
                if values[0] == 'v':
                    for d in values:
                        if d == 'v':
                            continue
                        self.cordenadasVert.append(float(d))
                if values[0] == 'vt':
                    for d in values:
                        if d == 'vt':
                            continue
                        self.coordenadasT.append(float(d))

                line = f.readline()

        for princiapL_vertex, Catalg in enumerate(self.coordenadasTotales):
            if princiapL_vertex % 3 == 2:
                self.BackUpVertices.extend(self.coordenadasN[(Catalg * 3):(Catalg * 3 + 3)])
            if princiapL_vertex % 3 == 0:
                self.BackUpVertices.extend(self.cordenadasVert[(Catalg * 3):(Catalg * 3 + 3)])
            if princiapL_vertex % 3 == 1:
                self.BackUpVertices.extend(self.coordenadasT[(Catalg * 2):(Catalg * 2 + 2)])

        self.matriz_principal = matriz_externa.array(self.BackUpVertices.copy(), dtype='float32')
