# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    back_to_start = False
    e = 100
    i = 0
    n = len(c)
    
    while not back_to_start:
        # jump
        i = (i + k) % n
        
        # calculate spent energy
        e -= 3 if c[i] else 1
        
        # evaluate if back to start
        back_to_start = i == 0
    
    return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
