# https://www.hackerrank.com/contests/projecteuler/challenges/euler009
# Difficulty: EASY

#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    products = [-1]
    
    # Brute force approach with O(n^3) time complexity
    # for i in range(1, n-1):
    #     for j in range(i+1, n):
    #         for k in range(j+1, n+1):
    #             if i + j + k == n and i**2 + j**2 == k**2:
    #                 products.append(i*j*k)

    # Better naive approach
    # for i in range(1, n-1):
    #     for j in range(i+1, n):
    #         k = n - (i + j)
    #         if i**2 + j**2 == k**2:
    #             products.append(i*j*k)

    # Given the following formulas
    #   a < b < c
    #   a^2 + b^2 = c^2
    #   a + b + c = N
    # we can make the following observations
    # - upper bound for `a`
    #   a < N / 3
    # - N^2 is even, hence `N` is even
    #   N^2 = 2a^2 + 2b^2 + 2ab + 2ac + 2bc
    # - formula for `b` given `a` and `N`
    #   b = (n^2 - 2an) / (2n - 2a)
    if n % 2 == 0:
        for a in range(1, (n // 3) + 1):
            b = (n**2 - 2*a*n) // (2*n - 2*a)
            c = n - (a + b)
            if a < b < c and a**2 + b**2 == c**2:
                products.append(a*b*c)
    
    print(max(products))