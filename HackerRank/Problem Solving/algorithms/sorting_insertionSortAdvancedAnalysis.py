#!/bin/python3

from bisect import bisect_right, insort
import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def insertionSort(arr):
    sorted_arr = [arr[0]]
    len_sorted = 1
    shift_count = 0
    for i in range(1, len(arr)):
        insort(sorted_arr, arr[i])
        sorted_idx = bisect_right(sorted_arr, arr[i])
        len_sorted += 1
        shift_count += len_sorted - sorted_idx
    return shift_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()