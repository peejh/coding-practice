# https://www.hackerrank.com/challenges/utopian-tree
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    h = 1
    cycle = 1 # 1 for spring, 0 for summer
    for _ in range(n):
        if cycle:
            h *= 2
            cycle = 0
        else:
            h += 1
            cycle = 1
    return h

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
