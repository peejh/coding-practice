# https://www.hackerrank.com/contests/projecteuler/challenges/euler004

#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    not_found = True
    
    while not_found and n > 101101:
        # get next palindrome less than N
        n -= 1
        if str(n) != str(n)[::-1]:
            continue

        # find if N can be a product of two 3-digit numbers
        for x in range(101, 999):
            y = n / x
            if y % 1 == 0 and y < 1000 and y > 100:
                not_found = False
                break
    
    print(n)