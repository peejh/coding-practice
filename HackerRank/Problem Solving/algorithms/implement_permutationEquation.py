#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    return [p.index(p.index(i)+1) + 1 for i in range(1, len(p)+1)]

def permutationEquation_smarter(p):
    # insert an element at the beginning of the list
    p.insert(0, 0) # this works because 0 < p[i] < 51, which will not interfere
                   # with index look-up, and fixes the return value of index 0
    return [p.index(p.index(i)) for i in range(1, len(p))]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
