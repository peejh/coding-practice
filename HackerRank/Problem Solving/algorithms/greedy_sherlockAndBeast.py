# https://www.hackerrank.com/challenges/sherlock-and-the-beast
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    '''
    The approach is to construct the decent number
    based on the value of `n`
    '''
    
    fives = n // 3 # max number of 5s that can fit in `n`
    decent = "-1" # keep as string type because `n` values
                  # go outside integer bounds
    
    # Lead with the 5s instead of 3s to construct the max
    # possible decent number of length `n`
    for f in range(fives, -1, -1):
        threes = n - (f * 3)

        if threes % 5 == 0:
            decent = "5" * f * 3 + "3" * threes
            break
    
    print(decent)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)