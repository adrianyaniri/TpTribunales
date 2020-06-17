################################FUNCIONES########################################################################################
#################################################################################################################################
from tribunales import*

# Retorna una lista con las posiciones ordenadas al azar con todas las oficinas de un edificio
def posicionesAlAzar(pisos = 4, oficinas = 3):
  randPosList = []
  randPos = sample(range(0, pisos*oficinas), pisos*oficinas)
  i = 0
  for posPiso in sample(range(0, pisos), pisos):
    for posOficina in sample(range(0, oficinas), oficinas):
      randPosList.insert(randPos[i],[posPiso,posOficina])
      i += 1
  return randPosList

#Retorna un edificio de Tribunales con los juzgados cargados (tambien crea los juzgados)
#Cambien: Nombre de TDA Edificio de tribunales segun el suyo
def crearEdificioConJuzgados(dicJuzgados = None, pisos = 4, oficinas = 3):
  tribunal = Tribunales(pisos, oficinas) ##Cambien aca con el nombre de su TDA Tribunales
  randPos = posicionesAlAzar(pisos, oficinas)
  i = 0
  for juzgado in dicJuzgados:
    try:
      tribunal.establecerJuzgado(randPos[i][0], randPos[i][1], Juzgado(juzgado, dicJuzgados[juzgado]))
      i += 1
    except:
      print("Mas juzgados que oficinas, el Juzgado del Juez " + juzgado + " no se pudo ubicar en el edificio.")
  return tribunal

#Retorna una pila de expedientes con numeros desde numInicio hasta numInicio+cantidad
#Cambien: Nombre del TDA Expediente segun el suyo y los tipos de Fuero, Prioridad y Estado (Yo use enums)
def crearPilaExp(numInicio = 1, cant = 100):
  pilaExp = Stack()
  for i in range(numInicio,numInicio+cant+1):
    pilaExp.push(Expediente(i, Fuero(np.random.randint(0,5)), Prioridad(np.random.randint(0,2)), Estado(np.random.randint(0,2))))
  return pilaExp

#Carga pilas de expedientes al tribunal (crea las pilas tambien)
def cargarPilasExp(tribunal = None, dicJuzgados = None, cantPilas = 10, expPorPila = 100):
  nombreJuzgados = list(dicJuzgados.keys())
  for i in range(0,cantPilas):
    posJuzgado = sample(range(0, len(nombreJuzgados)-1), 1)[0]
    tribunal.mesaDeEntradas(crearPilaExp(i*expPorPila+1, expPorPila),nombreJuzgados[posJuzgado])

################################FUNCIONES########################################################################################
#################################################################################################################################


# Juzgados que conforman el edificio (Pares de Nombre:Cantidad Critica)
datosJuzgados = {"Gomez":40, #Juzgado del juez Gomez con 40 de cantidad critica
            "Perez":20,
            "Rodriguez":50,
            "Gonzalez":100,
            "Juarez":90,
            "Ramirez":20,
            "Sanchez":80,
            "Rivarola":60,
            "Mendez":50,
            "Medina":40,
            "Gutierrez":30,
            "Lopez":70
            }

pisosEdificio = 5
oficinasPorPiso = 6
#Creo el edificio
tribunal = crearEdificioConJuzgados(datosJuzgados, pisosEdificio, oficinasPorPiso)
#Le cargo 10 pilas de 1000 expedientes cada una
cargarPilasExp(tribunal, datosJuzgados, 10, 1000)

print(tribunal)

print()
for i in range(pisosEdificio):
  print("Cantidad de juzgados criticos del piso " + str(i) + ": " + str(tribunal.cantidadDeJuzgadosCriticos(i)))

print()
print("Juzgado menos recargado: " + str(tribunal.juzgadoMenosRecargado()))

print()
for juzgado in datosJuzgados:
  print("Ubicacion de juzgado del Juez " + juzgado + ": " + str(tribunal.buscaJuzgado(juzgado)))
