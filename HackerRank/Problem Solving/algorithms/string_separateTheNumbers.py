# https://www.hackerrank.com/challenges/separate-the-numbers

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # consider lengths up to half the length of s.
    # by starting at length of 1, we can return the
    # smallest increasing sequence when found.
    for l in range(1, (len(s) // 2) + 1):
        curr_len = l
        toks = [] # s will be split into tokens of length curr_len and store them here
        is_increasing = True
        
        i = 0 # index of the first digit of current token
        while i < len(s) and is_increasing:
            tok = s[i:i+curr_len] # extract token of length curr_len
            
            # condition 1: toks is not empty and the current token is not last token + 1
            # condition 2: current token does not have a leading zero
            if (toks and int(tok) != toks[-1] + 1) or (re.match(r'^0\d+', tok)):
                is_increasing = False
            else:
                toks.append(int(tok))
            
            # if current token is a 9..., increment curr_len
            i += curr_len
            if re.match('^9+$', tok):
                curr_len += 1
        
        # if we get here without this flag getting negated,
        # the extracted tokens are of incrementing sequence
        if is_increasing:
            print(f'YES {toks[0]}')
            return # exit method when incrementing sequence is found
            
    print('NO')

def separateNumbers(s):
    '''
    1. extract the first token of length k
    2. build the string to compare with s by continuously incrementing the first token
    3. if the built string is the same as s, the sequence is valid
    '''
    k = 1
    flag = False
    
    while k < len(s):
        n = int(s[:k])
        
        temp, i = str(n), 1
        while len(temp) < len(s):
            temp += str(n+i)
            i += 1
                
        if temp == s:
            flag = True
            break
        
        k += 1

    print(f"YES {n}" if flag else "NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
