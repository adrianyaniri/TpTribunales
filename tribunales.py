import numpy as np
from  juzgados import*


class Tribunales:
# funcion contructor recibe por parametro la cantidad de piso y cantOficinas
#crea usando la funcion array de numpy, un arreglo de N piso y M cantOficinas
    def __init__(self,pisos = None, oficinas = None):
        self.pisos = pisos
        self.oficinas = oficinas
        self.tribunales = np.empty((pisos,oficinas),Juzgado)

# retorna la cantidad de oficinas que tiene el edifico tribunale
    def cantPisos(self):
        return self.pisos

# retorna la cantidad de oficinas que tiene el edificio
    def cantOficinas(self):
        return self.oficinas

# indica el juzgado que esta en la oficina actual
    def oficinaActual(self,piso,oficina):

        return self.tribunales[piso][oficina]

# retorna si la ofcina esta vacia
#compara la ofcina con un None
    def oficinaVacia(self,oficina):
        return oficina !=None

# estable en juzgado en el piso y oficina pasado por parametros
    def establecerJuzgado(self,piso, of, juzgado):
        if not self.tribunales[piso][of]:
            self.tribunales[piso][of] = juzgado

    def criticoEnPiso(self,piso, oficina = 0):
        cant = 0
        print(oficina == len(self.tribunales[piso])-1)
        
        print(cant)

# retorna el juzgado con menos expediente del edificion
# usa un par de bucles for para recorrerlo
# utiliza la funcinon expedientePorTipo del TDA expedinte
    def juzgadoMenosRecargado(self):
      menosCargado = 0
      for i in range(self.cantPisos()):
        for j in range(self.cantOficinas()):
          actual = self.tribunales[i][j]
          if actual != None:
              normal,urgente = actual.expedientePorTipo()
              if urgente < menosCargado:
                  #menosCargado = urgente
                  piso = i
                  oficina = j
        return i,j

#busca al juez pasado por parametro, en el edificio

    def buscarJuez(self,juez):

        for i in range(len(self.tribunales)-1):
            for j in range(len(self.tribunales[0])-1):
                actual = self.tribunales[i][j]
                if actual != None:
                    if juez == self.tribunales[i][j].getNombre(): # obtine el nombre del juez
                        piso = i
                        oficina = j

        return piso, oficina
# Primero cargamos los resultados de buscarJuez con el str como parametro a las variables piso y oficina  para encontrar la oficina donde trabaja el juez ,
    # despues preguntamos si la pila de expedientes esta NO esta vacia y si NO es critico para darles todos los expedientes a ese juez ,
    #  sino realizamos el mismo procedimiento que buzcarJuez pero con juzgadoMenosCargado para saber que juez tiene menos urgentes , lo localizamos y le damos todos los expedientes
    def mesaDeEntrada(self,pilaExp, juez):
        piso, oficina = self.buscarJuez(juez)   #funcio para buscar al juez
        oficina = self.oficinaActual(piso,oficina) # obtiene la ofical actual
        while not pilaExp.estaVacia():
            if not oficina.esCritico():
                oficina.recibirExpediente(pilaExp.pop())
            else:
                piso2,oficina2 = self.juzgadoMenosRecargado()
                oficina = self.oficinaActual(piso2,oficina2)
                oficina.recibirExpediente(pilaExp.pop())


    def __repr__(self):
        return str(self.tribunales)
