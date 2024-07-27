# https://www.hackerrank.com/challenges/minimum-distances
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # TIME COMPLEXITY: O(n)
    # SPACE COMPLEXITY: O(n)
    
    last_i = {} # For storing last seen index of a num value
    min_i_distance = sys.maxsize
    
    # Traverse the array `a` and store the index for each num value
    # in the dictionary `last_i`
    for i, v in enumerate(a):
        # If a num value is already in dictionary `a`, find the
        # distance between the current index and the index where it
        # was last seen, and then compare the distance to the
        # current `min_i_distance`
        if v in last_i:
            min_i_distance = min(min_i_distance, i - last_i[v])
        # Store the current index as the last seen index of the
        # current num value
        last_i[v] = i
    
    # If `min_i_distance` is still set to its initial value, return -1
    # Else, return its current value
    return -1 if min_i_distance == sys.maxsize else min_i_distance    

def minimumDistances2(a):
    # TIME COMPLEXITY: O(2n)
    # SPACE COMPLEXITY: O(2n)   
    
    # STEP 1: Track all the indices for each number in `a`
    indices = defaultdict(list)
    # Store the indices of same number in a list
    for i, v in enumerate(a):
        indices[v].append(i)

    # STEP 2: Find the minimum distance between indices of
    # the same number
    distances = [] #
    
    for l in indices.values():
        # If the list of indices for a number is not more than 1,
        # no distance can be recorded
        if len(l) > 1:
            i_distances = [curr - prev for prev, curr in zip(l, l[1:])]
            # Record the minimum index distance for a number value in
            # `distances` list
            distances.append(min(i_distances))
    
    # If `distances` is not empty, return the smallest index distance
    # Else return -1
    return min(distances) if distances else -1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()