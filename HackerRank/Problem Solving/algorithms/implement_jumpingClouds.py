# https://www.hackerrank.com/challenges/jumping-on-the-clouds
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    jumps = 0
    i = 0
    last_idx = len(c) - 1
    
    # keep jumping while last index of `c` is not reached
    while i < last_idx:
        if i+2 <= last_idx and c[i+2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1
        
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
