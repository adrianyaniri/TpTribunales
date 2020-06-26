
from juzgados import*
from tribunales import*
from funAux import*



# configura los TDA expedientes
expediente1 = Expediente(130,Fuero.civil,Prioridad.urgente,Estado.enJuicio)
expediente2 = Expediente(120,Fuero.civil,Prioridad.normal,Estado.enJuicio)
expediente3 = Expediente(3,Fuero.comercial,Prioridad.normal,Estado.investigacion)
expediente4 = Expediente(4,Fuero.familiar,Prioridad.urgente,Estado.enJuicio)

# crea el juzgado
juzgado = Juzgado('lopez')
# carga los expediente al juzgado
juzgado.recibirExpediente(expediente2)
juzgado.recibirExpediente(expediente1)

#crea otro juzgado
juzgado2 = Juzgado('mas')
juzgado2.esCritico()



#carga los expedientes al juzgado
juzgado2.recibirExpediente(expediente4)
juzgado2.recibirExpediente(expediente3)


# crea una pila con expedientes
pilaExp = Stack()
pilaExp.push(expediente3)
pilaExp.push(expediente4)

#crea el tribunal con 4piso y 4 oficina
tribunal = Tribunales(4,6)

tribunal.establecerJuzgado(1,2,juzgado2)
tribunal.establecerJuzgado(1,1,juzgado)

print(tribunal.obtenerJuzgado(1,2).esCritico())
print(tribunal.criticosEnPiso(0))
