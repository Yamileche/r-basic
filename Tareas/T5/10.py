# Dado una lista de nombres de persona, escribe una función que los ordene de tres formas diferentes:
# A. De forma alfabética
# B. De forma alfabética invertida
# C. De nombre más corto al más largo.

nombres = ["Juan", "Maria", "Armando"]

def order(names = []):
    return sorted(nombres), sorted(nombres,reverse=True), sorted(nombres, key=len)

print(order(nombres))
