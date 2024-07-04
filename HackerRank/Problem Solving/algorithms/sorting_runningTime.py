# https://www.hackerrank.com/challenges/runningtime/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    '''
    counts the number of shifts in an insertion sort
    '''
    shift = 0
    for i in range(1, len(arr)):
        j = i
        key = arr[i]
        while j > 0 and arr[j-1] > key:
            arr[j] = arr[j-1]
            shift += 1
            j -= 1
        arr[j] = key
    return shift

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
