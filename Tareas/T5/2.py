# Crea una función que lea una frase de teclado y nos diga si es o no un palíndromo (frase que se lee igual de
# izquierda a derecha o al revés como por ejemplo “La ruta nos aportó otro paso natural”).

import re
from unicodedata import normalize

def is_palindrome(word):
    """
    Devuelve si una frase es palíndroma.
    Args:
    word: str
    Returns:
    isPalindrome: Booleano
    """
    if not type(word) == str:
        raise TypeError("no se ha ingresado un string")
    word = word.lower()
    
    word = word.replace(" ", "")
    word = word.replace(".","")
    word = word.replace(",", "")
    word = word.replace(";","")
    

    #Quitando acentos y demás
    word = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", word), 0, re.I)
    # -> NFC
    word = normalize( 'NFC', word)

    # Verificando que es palíndromo
    n = len(word)
    for i in range(int(n / 2)):
        if word[i] != word[n - (i + 1)]:
            return False
    return True

print(is_palindrome("La ruta nos aportó otro paso natural."))