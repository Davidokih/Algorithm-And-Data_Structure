import math

def prime_Number(n):
    if(n < 2):
        return False
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True

print(prime_Number(113))

def isPrime(n):
    if(n < 2):
        return False
    for i in range(2,10):
        if(n % i == 0):
            return False
    return True

print(isPrime(113))