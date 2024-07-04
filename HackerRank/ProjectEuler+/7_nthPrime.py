# https://www.hackerrank.com/contests/projecteuler/challenges/euler007
# Difficulty: EASY

#!/bin/python3

import time
import sys
from math import sqrt

def isPrime(n):
    if n < 4:
        return True
    
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

def getPrimes():
    '''
    Uses something close to the Sieve of Eratosthenes algorithm
    but takes less space.
    '''
    primes = [2, 3]
    for i in range(4, 104730):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    return primes

primes = getPrimes() # build list of primes

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    # METHOD 1: Find nth prime per iteration
    # O(1) space
    # O(t*n) time - takes 120 ms per iteration
    # i = 2
    # ans = 0
    # while n > 0:
    #     if isPrime(i):
    #         ans = i
    #         n -= 1
    #     i += 1 
    # print(ans)

    # METHOD 2: Build a list of primes and return prime
    #           at (n-1)th index
    # O(n) space
    # O(n log n) time - for building the list
    # O(1) time - takes 0.001 ms per iteration
    print(primes[n-1])