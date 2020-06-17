from condiciones import*

# funciones auxiliares



# funcion que recibe por parametro un expediente
# retorna si esta o no en jucio
def estaEnJucio(juzgado):
    return juzgado.estado == Estado.enJuicio
