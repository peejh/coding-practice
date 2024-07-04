# https://www.hackerrank.com/challenges/and-product

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'andProduct' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER a
#  2. LONG_INTEGER b
#

def andProduct(a, b):
    # STEP 1: get binary representations of `a` and `b`
    # strip leading bits of b to make it the same length as `a`
    a_bin = bin(a)[2:]
    b_bin = bin(b)[2:][-len(a_bin):]

    # STEP 2: extract identical leading bits from both
    lead_bits = ''
    for x, y in zip(a_bin, b_bin):
        if x != y:
            break
        lead_bits += x

    # STEP 3: append zeros to leading bits to make it of equal
    # length to `a`
    ans_bin = lead_bits + '0' * (len(a_bin) - len(lead_bits))
    return int(ans_bin, 2)

def andProduct_oneLiner(a, b):
    '''
    O(1) complexity
    '''
    return a & b & ~((1 << (b-a).bit_length()) - 1)    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = andProduct(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
