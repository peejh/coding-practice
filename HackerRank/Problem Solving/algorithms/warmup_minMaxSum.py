# https://www.hackerrank.com/challenges/mini-max-sum

#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    allsum = reduce(lambda x, y: x + y, arr)
    print(f'{allsum - arr[-1]} {allsum - arr[0]}')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)