# https://www.hackerrank.com/challenges/grid-challenge
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    row = len(grid)
    col = len(grid[0])
    
    # Sort the characters in each string alphabetically
    for i in range(row):
        grid[i] = sorted(list(grid[i]))
    
    # Check if characters in each column is arranged alphabetically
    for i in range(1, row):
        for j in range(col):
            if grid[i][j] < grid[i-1][j]:
                return 'NO'
    
    return 'YES'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()