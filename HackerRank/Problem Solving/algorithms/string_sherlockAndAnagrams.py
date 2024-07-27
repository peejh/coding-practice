# https://www.hackerrank.com/challenges/sherlock-and-anagrams
# Difficulty: MEDIUM

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from itertools import combinations
from math import comb

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Count substrings of same length and same set of characters
    anagrams = Counter(getSubstrings(s))
    
    # Count the number of ways the same substrings can be picked
    total = 0
    for k, v in anagrams.items():
        if v >= 1:
            total += comb(v, 2)
    
    return total

def getSubstrings(s):
    # Return sorted substrings so the same substrings can be
    # easily grouped and counted together
    for i, j in combinations(range(len(s)+1), 2):
        yield ''.join(sorted(s[i:j]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()