# Crea un diccionario que tenga por claves los números del 1 al 10 y como valores sus raíces cuadradas
from math import sqrt


d = dict()

for i in range(1, 10):
    d.setdefault(i, sqrt(i))

print(d)

