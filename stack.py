class Stack:

# funcion contrustor
  def __init__(self):
    self.pila =  []
# funcion que vacia la pila
  def vaciar(self):
    self.pila.clear()

# agrega un elemento
  def push(self,elemento):
    return self.pila.append(elemento)

# elimina un elemento
  def pop(self):
    pop = None
    if not self.estaVacia():
      pop = self.pila.pop()
    else:
      raise Exception('stack isEmpy')
    return pop

# muestra el elemento que esta al tope de la pila
  def top(self):
    dato = None
    if not self.estaVacia():
      dato = self.pila[len(self.pila)-1]
    else:
      raise Exception(' stack isEmpy')
    return dato

# clona una pila
  def clonar(self):
    clon = Stack()
    for elemento in self.pila:
     clon.pila.append(elemento)
    return clon
# retorna el tamanio de una pila

  def tamanio(self):
    return len(self.pila)

# incica si la pila tiene o no elementos
  def estaVacia(self):
    return len(self.pila) == 0

# funcion para mostar la pila
  def __repr__(self):
    return str(self.pila)
