# https://www.hackerrank.com/challenges/compare-the-triplets

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    result = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            result[0] += 1
        elif a[i] < b[i]:
            result[1] += 1            
    return result

def compareTriplets_v2(a, b):
    comps = [int(a[i] > b[i]) - int(a[i] < b[i]) for i in range(len(a))]
    print(comps)
    return [comps.count(1), comps.count(-1)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
