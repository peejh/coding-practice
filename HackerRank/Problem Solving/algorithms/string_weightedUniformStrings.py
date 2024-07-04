# https://www.hackerrank.com/challenges/weighted-uniform-string

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    weights = set()
    last = '@' # any non-lowercase character works
    last_cweight = 0
    cumulative_weight = 0
    
    for c in s:
        if c == last:
            cumulative_weight += last_cweight
        else:
            last_cweight = ord(c) - 96
            cumulative_weight = last_cweight
            last = c
        weights.add(cumulative_weight)
    
    return ['Yes' if q in weights else 'No' for q in queries]

def weightedUniformStrings2(s, queries):
    weights = set()
    last = None
    count = 1
    
    for c in s:
        count = 1 if c != last else (count + 1)
        weights.add((ord(c) - 96) * count)
        last = c

    return ['Yes' if q in weights else 'No' for q in queries]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
