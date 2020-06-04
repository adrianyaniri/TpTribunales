from cola import*
from expediente import*


# TDA tipo Juzgado

class Juzgado:
    def __init__(self,nombre):
        self.nombre = nombre
        self.urgente = Cola()
        self.normal =  Cola()

    def __repr__(self):
        cadena = 'nombre del juzgado: '+ self.nombre + '\n' + 'expedientes prioridad normal: '+str(self.normal) + '\n'+ 'expedientes prioridad urgente: '+str(self.urgente)
        return cadena

    def getJuzgado(self):
        return self


    def tieneNormal(self):
        return not self.normal.isEmpty()

    def tieneUrgentes(self):
        return not self.urgente.isEmpty()


    def recibirExpediente(self,expediente):
        cantCritica = 50
        if expediente.esNormal():
            self.normal.queue(expediente)
        else:
            self.urgente.queue(expediente)


        if self.normal.lenQueue() >= cantCritica:
            print('llego a la cantidad critica')
        if self.urgente.lenQueue() >= cantCritica:
            print('llego a la cantidad critica')


    def primerExpedienteATratar(self):
        exp = None

        if self.tieneUrgentes():
            exp = self.urgente.top()
        elif self.tieneNormal():
            exp = self.normal.top()
        else:
            raise Exception('no hay expediente')
        return exp

    def tratarExpediente(self):
        exp = None
        if self.tieneUrgentes():
            exp = self.urgente.dequeue()
        else:
            exp = self.normal.dequeue()
        return exp

    def cantidadTotalExp(self):
        sumNormal = self.normal.lenQueue()
        sumUrgente = self.urgente.lenQueue()
        return sumNormal + sumUrgente

    def expedientePorTipo(self):
        expNormal = self.normal.lenQueue()
        expUrgente = self.urgente.lenQueue()
        return 'total expedientes Normal:' , expNormal ,'total de expedientes Urgentes: ', expUrgente

    def esCritico(self):
        cantCritica = 1
        return self.urgente.lenQueue() > cantCritica or self.normal.lenQueue() > cantCritica

    def enJucio(self):
        auxUrgente = self.urgente.clonar()
        auxNormal = self.normal.clonar()
        cant = 0

        while not auxUrgente.isEmpty():
            if auxUrgente.top().estaEnJucio():
                cant += 1
            auxUrgente.dequeue()

        while not auxNormal.isEmpty():
            if auxNormal.top().estaEnJucio():
                cant += 1
            auxNormal.dequeue()
        return 'cantidad de expedientes en juicio: ', cant

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


    def buscarExpediente(self,nroExp):
        expediente = self.buscarExpedienteEn_(nroExp,self.normal)
        if not expediente:
            expediente = self.buscarExpedienteEn_(nroExp,self.urgente)
        return expediente

    def eliminarDe(self,nroExp,cola):
        aux = cola.clonar()
        aux2 = self.normal.clonar()
        cola.empty()
        self.normal.empty()

        while not aux.isEmpty():
            if aux.top().getNroExp() != nroExp:
                cola.queue(aux.top())

            aux.dequeue()

        while not aux2.isEmpty():
            if aux2.top().getNroExp() != nroExp:
                self.normal.queue(aux2.top())

            aux2.dequeue()

    def eliminarExpediente(self,nro):
        self.eliminarDe(nro,self.normal)
        self.eliminarDe(nro,self.urgente)


    def cambiar1(self,nroExp):
        exp = self.buscarExpediente(nroExp)
        exp.cambiarPrioridad()
        if exp.esNormal():
            self.normal.queue(exp)
        else:
            self.urgente.queue(exp)

    def cambiar(self,cola1,cola2,nroExp):
        cola1 = self.urgente
        cola2 = self.normal
        colaAux1 = Cola()
        colaAux2 = Cola()
        aux1 = None
        aux2 = None

        while not cola1.isEmpty():
            if cola1.top().getNroExpediente() == nroExp:
                cola.top().setPrioridad(Prioridad.urgente)
                aux1 = cola1.dequeue()
                colaAux2.queue(aux1)
            else:
                aux1 = cola1.dequeue()
                colaAux1.queue(aux1)

        while not cola2.isEmpty():
            if cola2.top().getNroExpediente() == nroExp:
                cola2.top().setPrioridad(Prioridad.normal)
                aux2 = cola2.dequeue()
                colaAux1.queue(aux2)
            else:
                aux2 = cola2.dequeue()
                colaAux2.queue(aux2)

        while not colaAux2.isEmpty():
            cola1.queue(colaAux2.dequeue())


        while not colaAux1.isEmpty():
            cola2.queue(colaAux1.dequeue())
