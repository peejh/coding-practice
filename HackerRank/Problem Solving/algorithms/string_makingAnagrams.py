# https://www.hackerrank.com/challenges/making-anagrams/

#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    s1 = Counter(s1)
    s2 = Counter(s2)
    delete_counter = 0
    
    for k, v1 in s1.items():
        delete_counter += abs(v1 - s2[k]) if k in s2 else v1
        # if k in s2:
        #     delete_counter += abs(v1 - s2[k])
        # else:
        #     delete_counter += v1
        
    for k, v2 in s2.items():
        delete_counter += v2 if k not in s1 else 0
        # if k not in s1:
        #     delete_counter += v2
        
    return delete_counter

def makingAnagrams_best(s1, s2):
    c1, c2 = Counter(s1), Counter(s2)    
    return (c1 - c2).total() + (c2 - c1).total()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
