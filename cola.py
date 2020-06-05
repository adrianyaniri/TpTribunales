# TDA cola

class Cola:
# funcion contructor
  def __init__(self):
    self.cola = []
# elimina todo los elemento de la cola
  def empty(self):
    self.cola.clear()
# encola un elemento en la cola
  def queue(self,item):
    self.cola.insert(0,item)
# desemcola el primer elemento de la cola
  def dequeue(self):
    data = None
    if not self.isEmpty():
      data = self.cola.pop()
    else:
      raise Exception('queue isEmpty')
    return data
# muestar el primer elemento de la cola
  def top(self):
    data = None
    if not self.isEmpty():
      data = self.cola[len(self.cola)-1]
    else:
      raise Exception('queque isEmpy')
    return data
# clona la cola
  def clonar(self):
    clon = Cola()
    for item in reversed(self.cola):
      clon.queue(item)
    return clon
# indica la cantidad elementoss
  def lenQueue(self):
    return len(self.cola)
#retorna si la cola esta vacia
  def isEmpty(self):
    return len(self.cola) == 0

  def __repr__(self):
    return str(self.cola)
