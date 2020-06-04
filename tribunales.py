import numpy as np
from  juzgados import*

class Tribunales:

    def __init__(self,pisos = None, oficinas = None):
        self.pisos = pisos
        self.oficinas = oficinas
        self.tribunales = np.empty((pisos,oficinas),Juzgado)


    def cantPisos(self):
        return self.pisos

    def cantOficinas(self):
        return self.oficinas


    def establecerJuzgado(self,piso, of, juzgado):
        if not self.tribunales[piso][of]:
            self.tribunales[piso][of] = juzgado

    def oficinaActual(self,piso,oficina):
        return self.tribunales[piso][oficina]

    def oficinaVacia(self,ofi):
        return not ofi == None


    def cantidadDeJuzgadosCriticos(self,piso):
        cantidad = None
        totalOficinas = 2
        if totalOficinas == 0:
            if self.oficinaVacia(self.oficinaActual(0,0)) and self.oficinaActual(0,0).esCritico():
                cantidad = 1
        else:
            cantidad = self.cantidadDeJuzgadosCriticos(piso)
        totalOficinas -=1

        return cantidad











    def __repr__(self):
        return str(self.tribunales)
