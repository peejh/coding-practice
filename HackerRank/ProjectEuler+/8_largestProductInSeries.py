# https://www.hackerrank.com/contests/projecteuler/challenges/euler008
# Difficulty: EASY

#!/bin/python3

import sys
from functools import reduce
from operator import mul

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    
    digits = [int(d) for d in str(num)]

    # calculate initial running product
    run_prod = reduce(mul, digits[:k])
    # initialize max product variable
    max_prod = run_prod
    
    for i in range(k, len(digits)):
        prev_digit = digits[i-k]
        
        # check if previous digit is zero
        # if yes, recalculate the running product starting
        #   on index after the zero digit
        # if no, remove the previous digit from the running
        #   product and multiply in the current digit
        if prev_digit == 0:
            run_prod = reduce(mul, digits[i-k+1:i+1])
        else:
            run_prod = (run_prod // prev_digit) * digits[i]

        # check if the new running product is higher than
        #   previous high
        max_prod = max(max_prod, run_prod)
    
    print(max_prod)