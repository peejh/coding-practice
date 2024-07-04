# https://www.hackerrank.com/challenges/reduced-string

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    adj_regex = re.compile(r'(.)\1')
    match = adj_regex.search(s)

    while match:
        s = s.replace(match.group(), '')
        match = adj_regex.search(s)

    return s if len(s) > 0 else "Empty String"

def superReducedString_recursive(s):
    if not s:
        return "Empty String"
    
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            reduced_s = s[:i] + s[i+2:]
            return superReducedString_recursive(reduced_s)
    
    return s 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
