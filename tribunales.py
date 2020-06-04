import numpy as np
from  juzgados import*

class Tribunales:

    def __init__(self,cantPiso = None, cantOf = None):
        self.cantPiso = cantPiso
        self.cantOf = cantOf
        self.tribunales = np.empty((cantPiso, cantOf),Tribunales)


    def establecerJuzgado(self,piso, of, juzgado):
        if not self.tribunales[piso][of]:
            self.tribunales[piso][of] = juzgado

    def getOficina(self):
        return self.tribunales[0][0]


    def cantidadDeJuzgadosCriticos(self,piso):
        cantidad = None
        oficina = self.tribunales[piso][0]
        if oficina.esCritico():
            cantidad = 1

        else:
            cantidad = cantidadDeJuzgadosCriticos(self,piso)
            self.tribunales[piso][1]
        return cantidad









    def __repr__(self):
        return str(self.tribunales)
