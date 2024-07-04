# https://www.hackerrank.com/challenges/cipher

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. STRING s
#

def cipher_best(k, s):
    '''
    > improves on other solutions when we realize that the bits in
    `s` embodies the XORs of the previous k bits
    > constructs the decoded binary string from left to right
    > O(n) space, O(n) time
    '''

    # this is perhaps uncessary since k is constrained to be >= 1
    # but the whole logic fails when k <= 0
    if k == 0:
        return s
        
    S = s[0]
    for i in range(1, len(s) - k + 1):
        S += str(int(s[i]) ^ int(s[i-1]) ^ (0 if i < k else int(S[i-k])))
    
    return S    

def cipher(k, s):
    '''
    > the idea is the same as the brute force method, except
    the previous k bits are not being tracked, hence no XORs
    of previous k bits is being calculated per iteration
    > calculated XORs of previous k bits is passed on to the
    next iteration, and the kth farthest bit is XORed out
    > constructs the decoded binary string from right to left
    '''

    # solution works even without this check, but maybe a
    # testcase where k = 1 is not present
    # if k == 1:
    #     return s
    
    len_orig = len(s) - k + 1
    s = [int(bit) for bit in s][::-1]
    ans = [s[0]]
    prev_xor = s[0]
    k_len = 1
    i = 1
    
    while len(ans) < len_orig:
        s_bit = s[i]
        ans_bit = prev_xor ^ s_bit

        if k_len == k-1:
            prev_xor = prev_xor ^ ans_bit ^ ans[i-k+1]
        else:
            prev_xor = prev_xor ^ ans_bit
            k_len += 1

        ans.append(ans_bit)
        i += 1
    
    ans.reverse()
    return ''.join(map(str, ans))

def cipher_bruteForce(k, s):
    '''
    > this solution has O(n*k) runtime because as we construct
    the answer, we are XORing the previous k elements
    > n is the length of the resulting binary number
    > k is the shift count, hence the k previous bits that when
    XORed together produces a bit in `s`
    > constructs the decoded binary string from right to left    
    '''
    
    len_orig = len(s) - k + 1 # the length of the decrypted binary string
    s = [int(bit) for bit in s][::-1] # convert to int list and reverse
    k_bits = [s[0]] # tracks the previous k-1 bits
    ans = [s[0]]    # the constructed answer
    i = 1           # start at 2nd index
    
    while len(ans) < len_orig:
        total_xor = s[i] # total XOR of current s-bit and previous k-1 bits
                         # this is also the decoded at bit at index i

        # track previous k-1 bits
        if len(k_bits) == k:
            k_bits = k_bits[1:]
        
        # get total XOR
        for prev in k_bits:
            total_xor ^= prev
        
        k_bits.append(total_xor)
        ans.append(total_xor)
        i += 1
    
    # reverse the decoded bits and concat to form the decoded binary string
    ans.reverse()
    return ''.join(map(str, ans))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = cipher(k, s)

    fptr.write(result + '\n')

    fptr.close()
