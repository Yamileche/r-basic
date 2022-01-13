# Crea una función que dados dos diccionarios nos diga qué claves están presentes en ambos.

def di(d1, d2):
    if not type(d1) == dict:
        raise TypeError("Entrada 1 no se ha ingresado dict")
    if not type(d2) == dict:
        raise TypeError("Entrada 2 no se ha ingresado dict")
    A1 = set(d1.keys())
    A2 = set(d2.keys())

    return A1.intersection(A2)

d = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", 
    "g": "--.", "h": "....", "i": "..", "j": "·---", "k": "-.-", "l": ".-..", 
    "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".__.", "q": "--.-",
    "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
    "x": "-..-", "y": "-.--", "z": "--..",
}


print(di(d,{"a":"", "w": ""}))