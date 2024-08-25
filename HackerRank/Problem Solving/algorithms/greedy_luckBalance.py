# https://www.hackerrank.com/challenges/luck-balance
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Separate luck based on importance
    importants = []
    nonimportants = []    
    for luck, importance in contests:
        if importance == 1:
            importants.append(luck)
        else:
            nonimportants.append(luck)

    # Sort `importants` to make it easier to retrieve
    # the `k` highest lucks
    importants.sort(reverse=True)

    # Calculate `total_luck`
    # Add the `k` highest lucks of important contests that Lena can lose
    total_luck = sum(importants[:k])
    # Subtract the luck factor of important contests that Lena has to win
    total_luck -= sum(importants[k:])
    # Add the luck factor of non-important contests that Lena can lose
    total_luck += sum(nonimportants)
    
    return total_luck


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
