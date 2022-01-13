# Crea una función que reciba los tres coeficientes a, b y c para resolver una ecuación de segundo grado.
# Muestra la solución por pantalla y ayúdate de la librería math para acceder a la función raíz cuadrada.
from cmath import sqrt
def chicharronera(a,b,c):
    det = b**2 -4*a*b
    if a == 0:
        if b == 0:
            if c != 0:
                print("La ecuación no tiene solución")
                return 
            else:
                print("Cualquier número es solución")
                return 0
        else:
            return -c/b
    else:
        return (-b+sqrt(b**2-4*a*c))/(2*a), (-b-sqrt(b**2-4*a*c))/(2*a)

print(chicharronera(0,1,1))