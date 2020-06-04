# TDA cola

class Cola:

  def __init__(self):
    self.cola = []

  def empty(self):
    self.cola.clear()

  def queue(self,item):
    self.cola.insert(0,item)

  def dequeue(self):
    data = None
    if not self.isEmpty():
      data = self.cola.pop()
    else:
      raise Exception('queue isEmpty')
    return data

  def top(self):
    data = None
    if not self.isEmpty():
      data = self.cola[len(self.cola)-1]
    else:
      raise Exception('queque isEmpy')
    return data

  def clonar(self):
    clon = Cola()
    for item in reversed(self.cola):
      clon.queue(item)
    return clon

  def lenQueue(self):
    return len(self.cola)

  def isEmpty(self):
    return len(self.cola) == 0

  def __repr__(self):
    return str(self.cola)
