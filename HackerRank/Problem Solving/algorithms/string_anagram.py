# https://www.hackerrank.com/challenges/anagram

#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # if length of s is odd, it cannot be split evenly
    if len(s) % 2 == 1:
        return -1
    
    half = len(s) // 2
    half1, half2 = s[:half], s[half:] # extract halves
    
    # STEP 1: count letters in each half
    half1_dict = {}
    half2_dict = {}
    
    for c in half1:
        half1_dict[c] = half1_dict[c] + 1 if c in half1_dict else 1
    for c in half2:
        half2_dict[c] = half2_dict[c] + 1 if c in half2_dict else 1
    
    # STEP 2: count the number of changes that has to be made in either half
    change_count = 0
    
    for k, v1 in half1_dict.items():
        if k in half2_dict:
            v2 = half2_dict[k]
            change_count += (v1 - v2) if v1 > v2 else 0
        else:
            change_count += v1

    return change_count

def anagram_v2(s):
    # if length of s is odd, it cannot be split evenly
    if len(s) % 2 == 1:
        return -1
    
    half = len(s) // 2
    
    # STEP 1: count letters in each half
    half1 = Counter(s[:half])
    half2 = Counter(s[half:])
    
    # STEP 2: count the number of changes that has to be made in either half
    change_count = 0
    
    for k, v1 in half1.items():
        if k in half2:
            v2 = half2[k]
            change_count += (v1 - v2) if v1 > v2 else 0
        else:
            change_count += v1

    return change_count    

def anagram_best(s):
    if len(s) % 2 == 1:
        return -1
    
    half = len(s) // 2
    half1 = Counter(s[:half])
    half2 = Counter(s[half:])
    
    return (half1 - half2).total()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
