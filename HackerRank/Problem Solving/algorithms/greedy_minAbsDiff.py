# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # The minimum difference can be found between adjacent
    # elements in a sorted array

    arr.sort()
    min_diff = sys.maxsize
    
    for i in range(1, len(arr)):
        min_diff = min(min_diff, abs(arr[i] - arr[i-1]))

    return min_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
