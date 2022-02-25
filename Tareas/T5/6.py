# Crea una función que dado un número N nos diga si es primo o no (tiene que ir dividiendo por todos los
# números x comprendidos entre 2 y el número N − 1 y ver si la división de N
# x tiene resto cero o no).

from math import fabs, sqrt
primes = []
def is_prime(p):
    if not type(p) == int or int(p) != p:
        raise TypeError("No se ha ingresado un int")
    p = fabs(p)
    

    if p == 1 or p % 2 ==0 or p % 3 == 0: return False
    
    primes.append(2)
    primes.append(3)
    primes.append(5)
    k = 6
    l=0
    while(k +1 <= p or k + 5 <= p):
        es_primo1 = True
        es_primo2 = True
        for i in primes:
            if (k + 1) % i== 0 == 0:
                es_primo1 = False
            if (k + 5) % i == 0:
                es_primo2 = False
        if es_primo1:
            primes.append(k + 1)
 
            if p%(k+1) == 0:
                return False
            if p == k + 1:
                return True
            

        if es_primo2:
            primes.append(k + 5)
            if k + 5 > sqrt(p):
                return True
            if p%(k+5) == 0:
                return False
            if p == k + 5:
                return True

        k +=6
    return False

print(is_prime(982451653))


sq