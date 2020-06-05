# TDA tipo expediente
from condiciones import*



class Expediente:
    # contructor
    def __init__(self,nroExpediente = 0,fuero = Fuero.civil,prioridad = Prioridad.normal,estado = Estado.investigacion):
        self.nroExpediente = nroExpediente
        self.fuero = fuero
        self.prioridad = prioridad
        self.estado = estado

# obtiene la priodidad del expediente
    def getPrioridad(self):
        return self.prioridad

# retorna el fuero del expediente
    def getFuero(self):
        return self.fuero

# indica si el expediente tiene prioridad normal
    def esNormal(self):
        return self.prioridad == Prioridad.normal

# obtiene el numero del expediente
    def getNroExp(self):
        return  self.nroExpediente

# retorna si el estado del expediente es enJucio
    def estaEnJucio(self):
        return self.estado == Estado.enJuicio

    def __repr__(self):
        cadena = 'nro Expediente: ' + str(self.nroExpediente) + '\nfuero de la causa: '+ str(self.fuero.name) + '\nprioridad: ' +  str(self.prioridad.name) +'\nestado de la causa: ' + str(self.estado.name)
        return cadena

#cambia la prioridad del expediente
    def cambiarPrioridad(self):
        if self.esNormal():
            self.prioridad = Prioridad.urgente
        else:
            self.prioridad = Prioridad.normal
