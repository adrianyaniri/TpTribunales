from enum import Enum

# class para declarar el tipo fuero de un expediente
class Fuero(int, Enum):
    civil = 1
    penal = 2
    laboral = 3
    familiar = 4
    comercial = 5

# class para determinar la prioridad del expediente
class Prioridad(int,Enum):
    normal = 1
    urgente = 2

# class para determina el estado del expediente
class Estado(int,Enum):
    investigacion = 1
    enJuicio = 2
