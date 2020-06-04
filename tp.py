
from juzgados import*
from tribunales import*

expediente1 = Expediente(130,Fuero.civil,Prioridad.urgente,Estado.enJuicio)
expediente2 = Expediente(120,Fuero.civil,Prioridad.normal,Estado.enJuicio)
expediente3 = Expediente(3,Fuero.comercial,Prioridad.normal,Estado.investigacion)
expediente4 = Expediente(4,Fuero.familiar,Prioridad.urgente,Estado.enJuicio)
juzgado = Juzgado('lopez')
juzgado.recibirExpediente(expediente2)
juzgado.recibirExpediente(expediente1)
juzgado.recibirExpediente(expediente4)
juzgado.recibirExpediente(expediente3)





tribunal = Tribunales(cantPiso= 2, cantOf = 3)
tribunal.establecerJuzgado(0,0,juzgado)
tribunal.establecerJuzgado(0,1,juzgado)
#oficina = tribunal.getOficina()
#print(oficina.esCritico())
print(tribunal.cantidadDeJuzgadosCriticos(0))
