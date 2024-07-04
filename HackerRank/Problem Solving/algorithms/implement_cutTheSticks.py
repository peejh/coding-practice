# https://www.hackerrank.com/challenges/cut-the-sticks
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    '''
    There is no need to subtract the smallest height from the
    higher heights per each iteration. Just filter out the
    smallest height each time until `arr` is empty.
    '''
    
    res = []
    
    while len(arr) > 0:
        res.append(len(arr))
        min_height = min(arr)
        arr = list(filter(lambda x: x != min_height, arr))
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()