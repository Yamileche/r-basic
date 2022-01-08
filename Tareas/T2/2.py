# Escribe una secuencia de instrucciones que permitan leer un número real por pantalla y que muestre si el
# número está en el rango entre −5 y 5, ambos incluidos.

numero = float(input("Ingrese un número real: "))

if numero >= -5 and numero <= 5:
    print("El número está en el rango deseado")
else:
    print("No está en el rango deseado")