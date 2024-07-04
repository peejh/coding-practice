# https://www.hackerrank.com/challenges/sum-vs-xor

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    count = 0
    for i, v in enumerate(range(n, n*2+1)):
        if i + v == i ^ v:
            count += 1
    return count

def sumXor2(n):
    count = 0
    for i, v in enumerate(range(n, n*2+1)):
        if i ^ v == n:
            count += 1
    return count

def sumXor_best(n):
    if n == 0:
        return 1
    binary = bin(n).replace("0b", "")
    zeros = sum([int(digit) == 0 for digit in binary])
    return 2 ** zeros

def sumXor_oneLiner(n):
    # lstrip removes given characters that are leading
    return 2 ** (bin(n).lstrip("0b").count('0'))
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
