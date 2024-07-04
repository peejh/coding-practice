# https://www.hackerrank.com/contests/projecteuler/challenges/euler003
# Difficulty: EASY

#!/bin/python3

import math


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    k = 2
    m = 1
    sqrt = int(math.sqrt(n))

    # if the highest prime factor is not n itself,
    # n and k converges to the highest prime factor
    while n != 1 and k <= sqrt:
        if n % k == 0:
            m = k
            n = n // k
            continue
        k = k + 1
        
    print(max(m, n))