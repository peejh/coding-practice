# https://www.hackerrank.com/contests/projecteuler/challenges/euler006
# Difficulty: EASY

#!/bin/python3

import sys
from functools import reduce


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    # Approach 1
    # sum_of_squares = 0
    # for i in range(1, n+1):
    #     sum_of_squares += i ** 2
    
    # Approach 2
    # sum_of_squares = reduce(lambda acc, x: acc + x ** 2, range(1, n+1))
    
    # Approach 3
    # sum_of_squares = sum(map(lambda x: x ** 2, range(1, n+1)))
    
    # Approach 4
    # sum_of_squares = sum([i ** 2 for i in range(1, n+1)])
    
    # Sum of first n squares formula
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    
    square_of_sum = (n * (n + 1) // 2) ** 2
    
    print(abs(sum_of_squares - square_of_sum))