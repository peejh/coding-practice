# https://www.hackerrank.com/challenges/maximum-perimeter-triangle
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # STEP 1: Find all valid triangles using the given
    # lengths from `sticks`
    sticks.sort()
    valid_triangles = set()
    for a, b, c in combinations(sticks, 3):
        if a + b > c:
            valid_triangles.add((a, b, c))
        
    # STEP 2: Return -1 if there are no valid triangles
    if len(valid_triangles) == 0:
        return [-1]
    
    # STEP 3: Sort `valid_triangles` per the given criteria
    valid_triangles = list(valid_triangles)
    valid_triangles.sort(key=lambda x: (x[2], x[0]), reverse=True)
    
    return valid_triangles[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()