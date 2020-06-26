from condiciones import*
from juzgados import*

# funciones auxiliares



# funcion que recibe por parametro un expediente
# retorna si esta o no en jucio
def estaEnJucio(juzgado):
    return juzgado.estado == Estado.enJuicio


def estaVacia(oficina):
    return oficina == None
