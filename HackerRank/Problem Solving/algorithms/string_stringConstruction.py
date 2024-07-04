# https://www.hackerrank.com/challenges/string-construction

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringConstruction(s):
    p = s[0]
    i = 1
    total_cost = 1

    while i < len(s):
        length = 1
        curr = s[i:]
        cost = 1

        for l in range(len(p),0,-1):
            substr = s[i:i+l]
            if re.search(substr, p):
                length = l
                cost = 0
                break

        p += s[i:i+length]
        total_cost += cost
        i += length

    return total_cost

def stringConstruction_iAmStupid(s):
    '''
    the point is, it is not required to append to by huge chunks of substrings.
    appending character by character is free, hence, all that's left is to 
    count how many unique characters the string s has.
    '''
    return len(set(s))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
