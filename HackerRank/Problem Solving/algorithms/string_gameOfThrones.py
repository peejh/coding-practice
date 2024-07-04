# https://www.hackerrank.com/challenges/game-of-thrones/

#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    c = Counter(s)
    even_count = [v % 2 == 0 for v in c.values()]
    is_all_even = all(even_count)
    is_one_odd = Counter(even_count)[False] == 1

    if is_all_even or is_one_odd:
        return 'YES'
    return 'NO'

def gameOfThrones_best(s):
    '''
    this solution uses O(1) space and has a more efficient O(n) runtime
    this returns 'NO' when an odd count has been encountered more than once
    '''
    c = Counter(s)
    odd_count_flag = False
    for v in c.items():
        if v % 2:
            if odd_count_flag:
                return 'NO'
            odd_count_flag = True
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
