# https://www.hackerrank.com/contests/projecteuler/challenges/euler001
# Difficulty: EASY

#!/bin/python3

import sys

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    
    # calculate the number of multiples up to n-1
    mult_three = (n - 1) // 3
    mult_five = (n - 1) // 5
    mult_fifteen = (n - 1) // 15
    
    # use arithmetic series formula to calculate sums of multiple
    #   3 + 6 + 9 + 12 + ...
    # = 3 x (1 + 2 + 3 + 4 + ... + n)
    # = 3 x (n x (n + 1) / 2)
    sum_three = 3 * mult_three * (mult_three + 1) // 2
    sum_five = 5 * mult_five * (mult_five + 1) // 2
    sum_fifteen = 15 * mult_fifteen * (mult_fifteen + 1) // 2
    
    # subtract the doubly counted multiples of both 3 and 5
    print(sum_three + sum_five - sum_fifteen)
