# https://www.hackerrank.com/challenges/equality-in-a-array
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    counts = Counter(arr)
    counts_max = max(counts.values())
    counts_sum = sum(counts.values())
    return counts_sum - counts_max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()