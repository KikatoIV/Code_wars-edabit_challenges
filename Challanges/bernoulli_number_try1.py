
from fractions import Fraction as Fr
from decimal import *
import math
pi = Decimal('3.141592653589793238462643383279502884197169399375105820974944592307816406286')

def factorial(Z):
    if Z == 0:
        return 1
    return Z*factorial(Z-1)

def prime_sve(m):
    prime_lst = []
    res = []
    for i in range(2, m+1 ):
        if i not in prime_lst:
            res.append(i)

            for j in range(i*i, m+1, i):
                prime_lst.append(j)
    return res

def bernoli_man(n):
    if(n == 1):
        return Fr(-1, 2)
    A = [0]*(n+1)
    for x in range(n+1):
        A[x] = Fr(1, 1+x)
        for j in range(x,0,-1):
            A[j-1] = j*(A[j-1] - A[j])
    return A[0]


def bernoulli_number(n):
    if n < 50:
        return bernoli_man(n)
    elif (n-1)%2 == 0:
        return 0 
    else:
        K = Decimal(2*(n)*factorial(n))/ (2*math.pi)**n
        primes = prime_sve(n+1)
        #d is sum of primes
        d = Decimal(1)
        for p in primes:
            if n%(p-1) == 0:
                d*= p
        
        N = math.ceil((K*d)**(1.0/(n-1)))
        z = 1

        for p in primes:
            if p <= N:
                z *= 1/(1-1/(p)**n)
        
        a = (-1)**(n/2 + 1)*Decimal((d*K*z))

        a = a.to_integral_exact(rounding=ROUND_HALF_EVEN)

        if a == 0:
            a = (-1)**(n/2+1)
        #print(a)
        #print(d)
        return Fr(a/d)

print(bernoulli_number(104))