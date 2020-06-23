from cola import*
from expediente import*
from stack import*
from funAux import*


# TDA tipo Juzgado

class Juzgado:
    # funcion contrictor
    def __init__(self,nombre,cant = 50 ):
        self.nombre = nombre # nombre del juez
        self.cantCritica = cant  # indica la cantidad de expedientes
        self.urgente = Cola()
        self.normal =  Cola()

    def __repr__(self):
        cadena = 'nombre del juzgado: '+ self.nombre + '\n' + 'expedientes prioridad normal: '+str(self.normal) + '\n'+ 'expedientes prioridad urgente: '+str(self.urgente)
        return cadena

# retorna el nombre del juez del juzgado2
    def getNombre(self):
        return str(self.nombre)

# retorna True si la cola normal tiene expedientes. False caso contrario
    def tieneNormal(self):
        return not self.normal.isEmpty()

# retorna True si la cola urgente tiene expeiente. False caso contrario
    def tieneUrgentes(self):
        return not self.urgente.isEmpty()

# recibe un expediente y lo agrega a la cola correspondiente
# informa si la cantida de expedinte de cada cola excede la cantidad critica
    def recibirExpediente(self,expediente):
        cantCritica = self.cantCritica
        if expediente.esNormal():
            self.normal.queue(expediente)
        else:
            self.urgente.queue(expediente)


        if self.normal.lenQueue() >= cantCritica:
            print('llego a la cantidad critica')
        if self.urgente.lenQueue() >= cantCritica:
            print('llego a la cantidad critica')

# retorna el primer expediente de la cola urgente
# si no hay expediente en la cola urgente, retorna el expediente de la cola normal
# si no hay expedientes en ninguna cola lanza una Exception
    def primerExpedienteATratar(self):
        exp = None

        if self.tieneUrgentes():
            exp = self.urgente.top()
        elif self.tieneNormal():
            exp = self.normal.top()
        else:
            raise Exception('no hay expediente')
        return exp

# retorna el primer expedinte a tratar de la cola urgente
# sino hay expediente en la cola urgente, busca en la cola norma
# elimina el expedinte de la cola donde esta
# si no hay ningun expediente lanza una Exception
    def tratarExpediente(self):
        exp = None
        if self.tieneUrgentes():
            exp = self.urgente.dequeue()
        else:
            exp = self.normal.dequeue()
        return exp

#devuelve la cantidad de expedinte que tiene el juzgado en ambas colas
    def cantidadTotalExp(self):
        sumNormal = self

# retorna la cantidad de expedinte que tienen cada cola
    def expedientePorTipo(self):
        expNormal = self.normal.lenQueue()
        expUrgente = self.urgente.lenQueue()
        return  expNormal , expUrgente

#retorna True si la cantidad de expedinte de cada cola supera la cantida critica
    def esCritico(self):
        cantCritica = self.cantCritica
        return self.urgente.lenQueue() > cantCritica or self.normal.lenQueue() > cantCritica

# funcion que recibe por parametro una cola y calcula cuanto expedientes en estado de jucio
    def enJucioEnExp(self,cola):
        aux = cola.clonar()
        cant = 0

        while not aux.isEmpty():
            if estaEnJucio(aux.top()):
                cant += 1
                aux.dequeue()
        return cant

# funcion que calcula cuantos expedientes esta en estado de Jucio
    def enJucio(self):
        return 'cantidad de Expediente en jucico: ',self.enJucioEnExp(self.urgente) + self.enJucioEnExp(self.normal)

# busca un expedinte por su numero en un cola pasada por parametro
# retorna el expedinte buscado
# sino lo encuentra retorna None
    def buscarExpedienteEn_(self,nroExp,cola):
        aux = cola.clonar()
        nro= None

        while not aux.isEmpty():
            if aux.top().getNroExp() == nroExp:
                nro = aux.top()
                aux.dequeue()
            else:
                aux.dequeue()
        return nro

# busca el expediente pasado por parametro en ambas colas del juzgado
#sino encuentra el expedinte retora None
#
    def buscarExpediente(self,nroExp):
        expediente = self.buscarExpedienteEn_(nroExp,self.normal)
        if not expediente:
            expediente = self.buscarExpedienteEn_(nroExp,self.urgente)
        return expediente

# elimina un expediente pasado por parmetro de la cola pasada por parametro

    def eliminarDe(self,nroExp,cola):
        aux = cola.clonar()
        cola.empty()
        while not aux.isEmpty():
            if aux.top().getNroExp() != nroExp:
                cola.queue(aux.top())

            aux.dequeue()


# elimina el expediente pasodo por parametro del las colas del juzgado
    def eliminarExpediente(self,nro):
        self.eliminarDe(nro,self.normal)
        self.eliminarDe(nro,self.urgente)

    def cambiarDeEstado(self,nro):
        exp = self.buscarExpediente(nro)
        exp.cambiarPrioridad()
        if exp.esNormal():
            self.normal.queue(exp)
            self.eliminarDe(nro,self.urgente)
        else:
            self.eliminarDe(nro,self.normal)
