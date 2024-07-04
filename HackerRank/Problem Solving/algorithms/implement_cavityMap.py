# https://www.hackerrank.com/challenges/cavity-map
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    n = len(grid)
    
    if n < 3:
        return grid
    
    modgrid = [[*nums] for nums in grid]
    
    # find cavities
    for i in range(1, n-1):
        for j in range(1, n-1):
            # order of comparison:
            # top, bottom, left, right
            if grid[i][j] > grid[i-1][j] and\
               grid[i][j] > grid[i+1][j] and\
               grid[i][j] > grid[i][j-1] and\
               grid[i][j] > grid[i][j+1]:
               modgrid[i][j] = 'X'
    
    # transform each row back into strings
    for i in range(n):
        modgrid[i] = ''.join(modgrid[i])
       
    return modgrid


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()