# https://www.hackerrank.com/contests/projecteuler/challenges/euler005

#!/bin/python3

import sys
from math import sqrt

def isPrime(n):
    '''
    Given a positive integer N, return
    TRUE if n is a prime number
    FALSE otherwise
    '''
    if n < 4:
        return True
        
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    # The smallest number X that can be divided by all numbers
    # from 1 to N is equal to the product of all primes p^k from
    # 1 to N, where k is the largest integer that meets the
    # condition p^k <= N

    prod = 1
    
    for i in range(2, n+1):
        if isPrime(i):
            k = 0
            while i ** (k+1) <= n:
                k += 1

            prod *= i ** k
    
    print(prod)