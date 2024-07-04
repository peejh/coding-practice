# UNSOLVED!

#!/bin/python3

from itertools import combinations
import math
import os
import random
import re
import sys

#
# Complete the 'countSubstrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. 2D_INTEGER_ARRAY queries
#

def countSubstrings(s, queries):
    counts = []
    
    for l, r in queries:
        substr = s[l:r+1]
        count = 0
        # print("------------------------")
        # print("SUBSTRING:", substr)
        for length in range(1, len(substr) + 1):
            combs = set()
            [combs.add(substr[i:i+length]) for i in range(len(substr)-length+1)]
            # print(combs)
            count += len(combs)
            # combs = set([''.join(c) for c in combinations(substr, length)])
            # valid = [1 if re.search(c, substr) else 0 for c in combs]
            # count += sum(valid)
        counts.append(count)

    return counts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    s = input()

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = countSubstrings(s, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
