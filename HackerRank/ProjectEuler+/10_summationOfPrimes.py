# https://www.hackerrank.com/contests/projecteuler/challenges/euler011
# Difficulty: MEDIUM

#!/bin/python3

import sys

def primeSums(n):
    '''
    Uses Sieve of Eratosthenes to find all primes up to a
    given `n`.
    Returns a list of cumulative sum of primes up to a
    given index.
    '''
    MAX_N = n + 1
    sieve = [True for _ in range(MAX_N)]
    sieve[0], sieve[1] = False, False
    for i in range(2, MAX_N):
        if sieve[i]:
            for j in range(i*2, MAX_N, i):
                sieve[j] = False
    
    cumulative_sums = [0]
    prev = 0
    for i in range(1, MAX_N):
        if sieve[i]:
            prev += i
        cumulative_sums.append(prev)
    
    return cumulative_sums


sum_of_primes = primeSums(1000000)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    # The solution is to pre-calculate a cumulative sum of
    # primes up to a given max constraint for `n`, which is
    # 10e6, and access the answer for each testcase
    print(sum_of_primes[n])