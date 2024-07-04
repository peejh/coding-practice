# https://www.hackerrank.com/challenges/xor-se

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the xorSequence function below.
def xorSequence(l, r):
    
    A = [0]
    for i in range(1, r+1):
        A.append(A[i-1] ^ i)
    
    ans = A[l]
    for n in A[l+1:]:
        ans ^= n
    
    return ans    

def xorSequence_betterMemory(l, r):

    curr = 0
    i = 1
    while i < l:
        curr = curr ^ i
        i += 1

    total = 0
    while i < r+1:
        curr ^= i
        total ^= curr
        i += 1
    
    return total

def xorSequence_calculate_v1(l, r):
    '''
    still times out in big testcases
    '''
    total = 0
    for i in range(l, r+1):
        total ^= getXor(i)
    return total
    
def getXor(i):
    ans = [i, 1, i+1, 0]
    return ans[i % 4]

def xorSequence_calculate_v2(l, r):
    '''
    best version which requires 1 XOR calculation
    '''
    return getXorI(r) ^ getXorI(l-1)

def getXorI(i):
    ans = [i, i, 2, 2, i+2, i+2, 0, 0]
    return ans[i % 8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        lr = input().split()

        l = int(lr[0])

        r = int(lr[1])

        result = xorSequence(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
