"""
    2) Consider a positive number n. Determine all its decompositions as sums of prime numbers.
"""

import math
from copy import deepcopy

def sieve(n):
    l = [True for _ in range(n)]
    
    l[0] = False
    l[1] = False
    for i in range(2,int(math.sqrt(n))+1):
        if l[i]:
            for j in range(i*i,n,i):
                l[j] = False

    return l

def get_primes(n):
    primes = []
    sieve_list = sieve(n)

    for i in range(2,len(sieve_list)):
        if sieve_list[i]:
            primes.append(i)

    return primes

def backtrack(n,primes,sol):
    if n < 0:
        return

    if n == 0:
        print(sol)
        return

    for prime in primes:
        sol.append(prime)
        backtrack(n - prime,primes,deepcopy(sol))
        sol.pop()
    

n = int(input('n='))
backtrack(n,get_primes(n),[])
    
