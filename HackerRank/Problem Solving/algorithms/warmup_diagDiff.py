# https://www.hackerrank.com/challenges/diagonal-difference

#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    left_diag = []
    right_diag = []
    for i in range(len(arr)):
        left_diag.append(arr[i][i])
        right_diag.append(arr[i][-1-i])
    left_sum = reduce(lambda x, y: x + y, left_diag)
    right_sum = reduce(lambda x, y: x + y, right_diag)
    return abs(left_sum - right_sum)

# uses O(1) space
def diagonalDifference_v2(arr):
    result = 0
    for i in range(len(arr)):
        result += arr[i][i] - arr[i][-1-i]
    return abs(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
