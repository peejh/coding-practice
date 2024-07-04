# https://www.hackerrank.com/challenges/flipping-bits

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    binary = list(bin(n).lstrip("0b").zfill(32))
    for i in range(len(binary)):
        binary[i] = '0' if binary[i] == '1' else '1'
    flipped = ''.join(binary)
    return int(flipped, 2)
    
def flippingBits_oneLiner(n):
    return int(''.join('1' if bit == '0' else '0' for bit in format(n, "032b")), 2)

def flippingBits_calculate(n):
    number = (2 ** 32) - 1
    # print(format(number, '032b'))
    # print(format(n, '032b'))
    # print(format(number - n, '032b'))
    return number - n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
