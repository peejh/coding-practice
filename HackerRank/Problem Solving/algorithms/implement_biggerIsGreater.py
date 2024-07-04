# https://www.hackerrank.com/challenges/bigger-is-greater
# Difficulty: MEDIUM

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    c = list(w) # turn to list to allow reassignments
    
    # start pivot index from 2nd last
    for i in range(len(c)-2, -1, -1):
        # compare pivot index to each index after it.
        # move from last index towards the pivot index
        for j in range(len(c)-1, i, -1):
            if c[i] < c[j]:
                c[j], c[i] = c[i], c[j] # switch
                unchanged = ''.join(c[:i+1]) # includes the pivot index
                minimized = ''.join(sorted(c[i+1:])) # sort the rest
                return unchanged + minimized
    
    return 'no answer'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
