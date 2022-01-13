# Crea una función que dado un número N nos diga si es primo o no (tiene que ir dividiendo por todos los
# números x comprendidos entre 2 y el número N − 1 y ver si la división de N
# x tiene resto cero o no).

from math import fabs, sqrt
def is_prime(p):
    if not type(p) == int or int(p) != p:
        raise TypeError("No se ha ingresado un int")
    p = fabs(p)
    
    if p == 2 or p == 3 or p == 5 or p == 7 or p == 11 or p == 13 or p == 17: return True
    if p == 1 or p % 2 ==0: return False
    primes = []
    primes.append(2)
    k = 4
    l=0
    while(k +1 <= p):
        es_primo1 = True
        print(k+1)
        for i in range(1,len(primes[:l-1])):
            if primes[i] % k + 1 == 0:
                es_primo1 == False


        if es_primo1:
            primes.append(k + 1)
            if p/17 <= k+1:
                return True
            else:
                l = len(primes)
            if p == k + 1:
                return True
        if sqrt(p)<k+1: return False
        k +=4
    
    l=0
    while(k + 3 <= p):
        es_primo1 = True
        print(k+3)
        for i in range(1,len(primes[:l-1])):
            if primes[i] % k + 3 == 0:
                es_primo1 == False


        if es_primo1:
            primes.append(k + 3)
            if p/17 <= k+3:
                return True
            else:
                l = len(primes)
            if p == k + 3:
                return True
        if sqrt(p)<k+3: return False
        k +=4



    return False


print(is_prime(97283421454511454131))
