import numpy as np
from  juzgados import*
from funAux import*
from expediente import*


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


# estable en juzgado en el piso y oficina pasado por parametros
    def establecerJuzgado(self,piso , of , juzgado):
        if not self.tribunales[piso][of]:
            self.tribunales[piso][of] = juzgado

# funcion que retorna el juzgado que se encuentra en el piso y oficina pasada por parametros

    def obtenerJuzgado(self,piso,oficina):
        return self.tribunales[piso][oficina]


#indica la cantidad de juzgados critricos que hay un piso
# primero compara si las oficinas estan vacias
# despues si es juzgado esta en estado critico
# con la recursiva calcula el total de oficinas criticas que hay en el piso
    def criticosEnPiso(self,piso = 0 , oficina = 0):
        cant = None
        if oficina == len(self.tribunales[piso])-1:
            if not estaVacia(self.obtenerJuzgado(piso,oficina)) and self.obtenerJuzgado(piso,oficina).esCritico():
                cant = 1
            else:
                cant = 0
        else:
            if not estaVacia(self.obtenerJuzgado(piso, oficina)) and self.obtenerJuzgado(piso,oficina).esCritico():
                cant = self.criticosEnPiso(piso, oficina + 1) +1
            else:
                cant = self.criticosEnPiso(piso,oficina +1)
        return cant




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
        return piso, oficina

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
        oficina = self.obtenerJuzgado(piso,oficina) # obtiene la ofical actual
        while not pilaExp.estaVacia():
            if not oficina.esCritico():
                oficina.recibirExpediente(pilaExp.pop())
            else:
                piso2,oficina2 = self.juzgadoMenosRecargado()
                oficina = self.oficinaActual(piso2,oficina2)
                oficina.recibirExpediente(pilaExp.pop())

   # def moverExp(nroExp, juezOrigen, juezDestino):
   # recibe por parametro un nro de expediente y un juez origen , un juez de destino
   # y cambia el expediente de la posicion
   # elimina el expendiente del juez original
    def moverExpediente(self,nro, juezOrigen, juezDestino):
        juezDestino.recibirExpediente(juezOrigen.buscarExpediente(nro))
        juezOrigen.eliminarExpediente(nro)

    def __repr__(self):
        return str(self.tribunales)
