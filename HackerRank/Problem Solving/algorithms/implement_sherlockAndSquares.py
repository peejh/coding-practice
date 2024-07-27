# https://www.hackerrank.com/challenges/sherlock-and-squares
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys
from math import sqrt

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    '''
    This solution reduces the number of iteration from `b-a`
    to the number of squares from `a` to `b`
    '''
    
    i = int(sqrt(a)) + 1
    # check if `a` is a square
    squares_count = 1 if sqrt(a) % 1 == 0 else 0

    while (i * i) <= b:
        squares_count += 1
        i += 1
    
    return squares_count

def squares_bruteforce(a, b):
    '''
    this solutions fails time limit
    '''
    squares_count = 0

    for i in range(a, b+1):
        if sqrt(i) % 1 == 0:
            squares_count += 1

    return squares_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
