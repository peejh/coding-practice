# https://www.hackerrank.com/contests/projecteuler/challenges/euler002
# Difficulty: EASY

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    # the nth term of even fibonacci numbers is given by
    #   F(n) = 4 * F(n-1) + F(n-2)
    # where the 1st and 2nd terms are 0 and 2

    even_fib1 = 0
    even_fib2 = 2
    total = even_fib1
    
    while even_fib2 <= n:
        total += even_fib2
        even_fib3 = 4 * even_fib2 + even_fib1
        even_fib1, even_fib2 = even_fib2, even_fib3
    
    print(total)