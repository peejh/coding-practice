# https://www.hackerrank.com/challenges/countingsort2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    MAX_VALUE = 100
    freq = [0 for _ in range(MAX_VALUE)]
    # count
    for num in arr:
        freq[num] += 1
    # overwrite arr
    i = 0
    for f in range(MAX_VALUE):
        for _ in range(freq[f]):
            arr[i] = f
            i += 1
    return arr
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
