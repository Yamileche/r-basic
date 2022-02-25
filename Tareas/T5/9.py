# Investiga el Cifrado del César y crea una función que lo reproduzca en Python. Cada letra del mensaje
# original se desplaza tres posiciones en el alfabeto estándar. La A se convierte en la D, la B se convierte en la
# E, la C se convierte en la F. . . y cuando se acaba el alfabeto se le vuelve a dar la vuelta: la X se convierte
# en la A, la Y en la B y la X en la C. Los números no sufren ninguna modificación

from string import ascii_lowercase


minu = list(ascii_lowercase.translate(range(65, 91)))
minu.insert(14,"ñ")

def ces_3(word):
    word1 = ""
    for i in word:
        if i == " ":
            word1 += " "
        elif i.lower() in minu:
            index = (minu.index(i.lower()) + 3) % 27 
            if i.isupper():
                word1 += minu[index].upper()
            else:
                word1 += minu[index]
        else:
            word += i

    return word1
