# https://www.hackerrank.com/challenges/two-characters

#!/bin/python3

from itertools import combinations
import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def is_alternating(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True

def alternate2(s):
    uniqs = set(s)

    if len(uniqs) < 2:
        return 0
        
    longest = 0
    for chars_out in combinations(uniqs, len(uniqs) - 2):
        word = s
        for char_out in chars_out:
            word = word.replace(char_out, "")
        if is_alternating(word):
            longest = max(longest, len(word))

    return longest

def alternate4(s):    
    uniqs = set(s)
    
    if len(uniqs) < 2:
        return 0     
        
    longest = 0
    alt_pattern = r'^(.)(?!\1)(.)(\1\2)*\1?$'   
    for comb in combinations(set(s), len(uniqs) - 2):
        word = s
        for char in comb:
            word = word.replace(char, '')
        if bool(re.match(alt_pattern, word)):
            longest = max(longest, len(word))
            
    return longest

def validate(s, okchars):
    last = '0'
    filtered = ""
    for c in s:
        if c not in okchars:
            continue
        if c == last:
            return None
        filtered += c
        last = c
    return filtered

def alternate(s):
    unique_chars = list(set(s))
    longest = 0

    for c1, c2 in combinations(unique_chars, 2):
        chars_in = c1 + c2
        valid = validate(s, chars_in)
        if valid:
            longest = max(longest, len(valid))

    return longest

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # l = int(input().strip())
    # s = input()
    # result = alternate(s)
    # fptr.write(str(result) + '\n')
    # fptr.close()

    print(alternate("beabeefeab")) # 5
    print(alternate("asdcbsdcagfsdbgdfanfghbsfdab")) # 8
    print(alternate("asvkugfiugsalddlasguifgukvsa")) # 0
    print(alternate("a")) # 0
    print(alternate("cwomzxmuelmangtosqkgfdqvkzdnxerhravxndvomhbokqmvsfcaddgxgwtpgpqrmeoxvkkjunkbjeyteccpugbkvhljxsshpoymkryydtmfhaogepvbwmypeiqumcibjskmsrpllgbvc")) # 8
    print(alternate("txnbvnzdvasknhlmcpkbxdvofimsvqbvkswlkrchohwuplfujvlwpxtlcixpajjpaskrnjneelqdbxtiyeianqjqaikbukpicrwpnjvfpzolcredzmfaznnzd")) # 6
    print(alternate("pvmaigytciycvjdhovwiouxxylkxjjyzrcdrbmokyqvsradegswrezhtdyrsyhg")) # 6
    print(alternate("muqqzbcjmyknwlmlcfqjujabwtekovkwsfjrwmswqfurtpahkdyqdttizqbkrsmfpxchbjrbvcunogcvragjxivasdykamtkinxpgasmwz")) # 6
    print(alternate("czoczkotespkfjnkbgpfnmtgqhorrzdppcebyybhlcsplqcqogqaszjgorlsrppinhgpaweydclepyftywafupqsjrbkqakpygolyyfksvqetrfzrcmatlicxtcxulwgvlnslazpfpoqrgssfcrfvwbtxaagjfahcgxbjlltfpprpcjyivxu")) # 6