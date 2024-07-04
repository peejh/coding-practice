# https://www.hackerrank.com/challenges/the-great-xor

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theGreatXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER x as parameter.
#

def theGreatXor(x):
    return findNextHighestPowerOfTwo(x) - x - 1
    
def findNextHighestPowerOfTwo(n):
    binaryOfN = bin(n).lstrip('0b')
    nextPowerOfTwo = '1' + ''.zfill(len(binaryOfN))
    return int(nextPowerOfTwo, 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        x = int(input().strip())

        result = theGreatXor(x)

        fptr.write(str(result) + '\n')

    fptr.close()
