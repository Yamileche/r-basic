# Escribe una secuencia de instrucciones que permitan leer un número entero y determinar si es cuadrado
# perfecto o no (piensa la mejor forma de hacerlo con lo que has aprendido hasta ahora)

from math import sqrt, floor
n = int(input("Ingrese un número entero: "))

if sqrt(n) == floor(sqrt(n)):
    print("El número es cuadrado perfecto")
else:
    print("El número no es cuadrado perfecto")