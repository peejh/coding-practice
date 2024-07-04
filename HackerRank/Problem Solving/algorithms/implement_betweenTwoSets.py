# https://www.hackerrank.com/challenges/between-two-sets

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # it's given that a and b are sorted
    lower = a[-1]
    upper = b[0]
    result = []
    for i in range(lower, upper + 1):
        if aDividesIntoNum(a, i) and numDividesIntoB(i, b):
            result.append(i)
    return len(result)
    # one liner
    # return sum([aDividesIntoNum(a, num) and numDividesIntoB(num, b) for num in range(max(a), min(b) + 1)])
    
def aDividesIntoNum(a, num):
    return all([num % i == 0 for i in a])

def numDividesIntoB(num, b):
    return all([i % num == 0 for i in b])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
