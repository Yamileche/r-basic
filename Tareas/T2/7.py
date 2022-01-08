# Busca la imagen de un tablero de ajedrez en Google y fíjate en la nomenclatura de las casillas. Escribe una
# secuencia que lea una letra y un número de teclado correspondiente a una casilla de un tablero de ajedrez y
# que indique si esta casilla es negra o blanca.

def square_color(number, letter):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    if not type(number) == int:
        raise TypeError("number tiene que ser un número entero")
    if not number in range(1,9):
        raise ValueError("number no está entre 1 y 8")
    if not type(letter) == str:
        raise TypeError("letter no es un string")
    letter = letter.lstrip().rstrip()
    if len(letter)>1:
        raise ValueError("Debe ser un sólo caracter")
    if letter.lower() not in letters:
        raise ValueError("letter no está en el conjunto de letras")
    
    m = letters.index(letter) + 1

    if number % 2 == 0 and m % 2 == 0:
        return "negro"
    elif number % 2 == 0 and m % 2 == 1:
        return "blanco"
    elif number % 2 == 1 and m % 2 == 0:
        return "blanco"
    else:
        return "negro"

letra = input("Ingrese la letra: ")
numero = int(input("Ingrese el número: "))
color =square_color(numero, letra)

print("La casilla es de color", color)