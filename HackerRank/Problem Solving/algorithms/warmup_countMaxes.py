# https://www.hackerrank.com/challenges/birthday-cake-candles

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    maxheight = 0
    countmax = 0
    for height in candles:
        if height > maxheight:
            maxheight = height
            countmax = 1
        elif height == maxheight:
            countmax += 1
    return countmax

def birthdayCakeCandles_v2(candles):
    maxheight = max(candles)
    return sum([1 if h == maxheight else 0 for h in candles])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
