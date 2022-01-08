# Escribe una secuencia de instrucciones que permitan leer las coordenadas de un punto (x, y) e indique en
# cuál de los cuatro cuadrantes se encuentra dicho punto.
# Si x = 0, deberás indicar que el punto se encuentra sobre el eje vertical.
# Si y = 0, deberás indicar que el punto se encuentra sobre el eje horizontal.
# Si tanto x = 0 como y = 0, entonces deberás indicar que el punto se trata del origen de coordenadas.

x = float(input("x="))
y = float(input("y="))

if x == 0 and y != 0:
    print("el punto se encuentra sobre el eje vertical")
elif x != 0 and y == 0:
    print("el punto se encuentra sobre el eje vertical")
elif x == 0 and y == 0:
    print("el punto se trata del origen de coordenadas")
