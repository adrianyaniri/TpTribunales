# TDA tipo expediente
from condicionesDelExpediente import*


class Expediente:
    def __init__(self,nroExpediente = 0,fuero = Fuero.civil,prioridad = Prioridad.normal,estado = Estado.investigacion):
        self.nroExpediente = nroExpediente
        self.fuero = fuero
        self.prioridad = prioridad
        self.estado = estado

    def getPrioridad(self):
        return self.prioridad

    def getFuero(self):
        return self.fuero

    def esNormal(self):
        return self.prioridad == Prioridad.normal


    def getNroExp(self):
        return  self.nroExpediente

    def estaEnJucio(self):
        return self.estado == Estado.enJuicio

    def __repr__(self):
        cadena = 'nro Expediente: ' + str(self.nroExpediente) + '\nfuero de la causa: '+ str(self.fuero.name) + '\nprioridad: ' +  str(self.prioridad.name) +'\nestado de la causa: ' + str(self.estado.name)
        return cadena

    def cambiarPrioridad(self):
        if self.esNormal():
            self.prioridad = Prioridad.urgente
        else:
            self.prioridad = Prioridad.normal
