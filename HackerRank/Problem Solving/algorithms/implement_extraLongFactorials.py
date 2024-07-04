# https://www.hackerrank.com/challenges/extra-long-factorials
# Difficulty: EASY

#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
from operator import mul

'''
NOTES:
The problem is when this implemented in C or C++, which
requires additional code to handle extra long integers.
'''

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    print(ans)

def extraLongFactorials_oneliner(n):
    print(reduce(mul, range(1, n+1)))

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)