# https://www.hackerrank.com/challenges/plus-minus

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    arrlen = len(arr)
    pos, neg, zer = 0, 0, 0
    for num in arr:
        if num > 0:
            pos += 1
        elif num == 0:
            zer += 1
        else:
            neg += 1
    print("{:.6f}".format(pos / arrlen))
    print("{:.6f}".format(neg / arrlen))
    print("{:.6f}".format(zer / arrlen))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
