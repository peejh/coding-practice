# https://www.hackerrank.com/challenges/capitalize/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split(' ')
    caps = list(map(lambda i: i.capitalize(), words))
    return ' '.join(caps)

def solveV2(s):
    toks = s.split(' ')
    caps = []
    for tok in toks:
        caps.append(tok.capitalize())
    return ' '.join(caps)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()        