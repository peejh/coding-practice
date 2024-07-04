# https://www.hackerrank.com/challenges/lilys-homework/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
    
def lilysHomework(arr):
    arr2 = [i for i in arr] # another copy is needed because arr will be modified
                            # when countSwaps is invoked
    sorted_arr = sorted(arr)
    sorted_reversed_arr = list(reversed(sorted_arr))
    swaps_in_ascending = countSwaps(arr, sorted_arr)
    swaps_in_descending = countSwaps(arr2, sorted_reversed_arr)
    
    return min(swaps_in_ascending, swaps_in_descending)
    
def countSwaps(arr, sorted_arr):
    # STEP 1: store indices of values in original array
    indices = dict()
    
    for i in range(len(arr)):
        if arr[i] not in indices:
            indices[arr[i]] = list()
        indices[arr[i]].append(i)
    
    # STEP 2: simulate sorting of original array, using sorted array
    #         as reference
    swap_count = 0
    
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            swap_count += 1
        
        # idea is to swap misplaced values to the current index
        # of the sorted value at i
        temp_idx = indices[sorted_arr[i]].pop() # extract index of sorted value
        indices[arr[i]].append(temp_idx) # track the index where wrong value will
                                         # be pushed
        arr[temp_idx] = arr[i] # push the wrong value to the current index of
                               # sorted value
        arr[i] = sorted_arr[i] # can be omitted; not necessary to swap back in
                               # the correct value
    
    return swap_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()