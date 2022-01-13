# Crea un diccionario que tenga como claves las letras del alfabeto castellano y como valores los símbolos del
# código morse (los tienes todos en la Wikipedia). A continuación crea una función que lea una frase del
# teclado y te la convierta a morse utilizando el diccionario anterior.


d = dict()

d = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", 
    "g": "--.", "h": "....", "i": "..", "j": "·---", "k": "-.-", "l": ".-..", 
    "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".__.", "q": "--.-",
    "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
    "x": "-..-", "y": "-.--", "z": "--..",
}

def word_to_morse(word):
    if not type(word) == str:
        raise TypeError("No se ha ingresado un str")
    word = word.lower()
    word.lstrip()
    word.rstrip()
    c = ""
    for i in word:
        if i != " ":
            c += d[i]
            c += " "

    return c

print(word_to_morse("Ya me quiero dormir"))