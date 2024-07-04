# https://www.hackerrank.com/challenges/maximizing-xor/

#!/bin/python3

from itertools import combinations
import math
import os
import random
import re
import sys

#
# Complete the 'maximizingXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def maximizingXor(l, r):
    xors = set()
    combs = combinations([n for n in range(l, r+1)], 2)
    for n1, n2 in combs:
        xors.add(n1 ^ n2)
    return max(xors)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
