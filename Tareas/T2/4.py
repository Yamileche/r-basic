# Escribe una secuencia de instrucciones que permitan leer dos números enteros y muestre el cociente de la
# división entera y el resto de la división entera.

a = int(input("Ingrese un entero: "))
b = int(input("Ingrese un entero: "))

q = a//b
r = a%b

print("cociente", q)
print("Resto", r)