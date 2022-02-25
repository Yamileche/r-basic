# Crea una función que calcule el máximo común divisor de dos números introducidos por el usuario por
# teclado.
from math import fabs
def mcd(a,b):
    r = 1
    a = int(fabs(a))
    b = int(fabs(b))
    if a == 0 or b == 0:
        return 1
    
    while(r!=0):
        r = a%b
        a = b
        b = r
    return a
a = int(input("Introduzca un número: "))
b = int(input("Introduzca un número: "))
print(mcd(a,b))

