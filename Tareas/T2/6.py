# Escribe una expresión que permita determinar si un número entero positivo puede corresponder a un año
# bisiesto o no. Se consideran años bisiestos aquellos cuyo número es divisible por cuatro excepto los años que
# son múltiplos de 100, a no ser que lo sean de 400 (por ejemplo el año 2000 fue bisiesto pero el 2100 no lo
# será).

def es_bisiesto(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return True
    return False

year = int(input("Ingrese un año: "))

if es_bisiesto(year):
    print("El año es bisiesto")
else:
    print("El año no es bisiestro")