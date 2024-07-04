# https://www.hackerrank.com/challenges/breaking-best-and-worst-records

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    best_score = worst_score = scores[0]
    best_broken = worst_broken = 0
    
    for s in scores[1:]:
        if s > best_score:
            best_score = s
            best_broken += 1
        elif s < worst_score:
            worst_score = s
            worst_broken += 1
    
    return [best_broken, worst_broken]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
