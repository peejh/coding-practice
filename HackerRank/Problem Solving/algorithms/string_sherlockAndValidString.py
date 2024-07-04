# https://www.hackerrank.com/challenges/sherlock-and-valid-string/

#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    freq = Counter(s)
    value_freq = Counter(freq.values())
    value_freq_keys = value_freq.keys()
    
    if len(value_freq_keys) == 1:
        return 'YES'
    elif len(value_freq_keys) == 2:
        # need ordering, so we dump value_freq to a list
        value_freq_list = [[k, v] for k, v in value_freq.items()]
        value_freq_list.sort(key=lambda x: x[1])
        # conditions
        value_freq_of_one_exists = value_freq_list[0][1] == 1
        value_freq_diffence_of_one = value_freq_list[0][0] - value_freq_list[1][0] == 1
        value_of_one = value_freq_list[0][0] == 1
        
        if value_freq_of_one_exists and (value_freq_diffence_of_one or value_of_one):
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()