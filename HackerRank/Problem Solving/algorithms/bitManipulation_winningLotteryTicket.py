# https://www.hackerrank.com/challenges/winning-lottery-ticket

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from math import comb

#
# Complete the 'winningLotteryTicket' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING_ARRAY tickets as parameter.
#

def winningLotteryTicket(tickets):
    '''
    > the idea is to convert the tickets into a binary form that
    tracks the existence of a digit (0-9) in a given ticket
    > when pairs of these binary forms are XORed against each other,
    a winning pair will return `1111111111` or 1023 in decimal
    > to avoid the O(n^2) runtime, the frequency of the binary forms
    are tracked instead since the possible values of the binary form
    only goes from 0 to 1023
    > this solution works since the objective is only to count the
    number of winning pairs, and not to identify which ticket pairs
    make a winning combination
    '''

    # STEP 1: convert the tickets into its binary representation and
    # track the frequency of the values
    win_count = 0
    freqs = Counter(map(binMap, tickets))
    
    # STEP 2: count the number of pairs that make a winning combination
    for i in range(1023): # notice the difference between this
        for j in range(i+1, 1024): # and this
            if i | j == 1023:
                win_count += (freqs[i] * freqs[j])
    
    # use a combination calculator to count the number of ways that
    # tickets represented as 1023 can make a winning pair with themselves
    win_count += comb(freqs[1023], 2)
    
    return win_count

def binMap(s):
    '''
    > maps a given number string into a binary representation that
    tracks the existence of a digit in the given number string.
    > converts the binary representation into an integer and returns it
    e.g.
    given `100582377`
    transforms into `1111010110`
        1 1 1 1 0 1 0 1 1 0
        0 1 2 3 4 5 6 7 8 9
    the `1111010110` representation is converted into the integer `982`
    '''

    s_bin = ['0' for _ in range(10)]
    for num in s:
        s_bin[int(num)] = '1'
    return int(''.join(s_bin), 2)

def winningLotteryTicket_bruteForce(tickets):
    n = len(tickets)
    win = set('0123456789')
    win_count = 0
    for i in range(n):
        curr = set(tickets[i])
        for j in range(i+1, n):
            if curr.union(set(tickets[j])) == win:
                win_count += 1
    return win_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    tickets = []

    for _ in range(n):
        tickets_item = input()
        tickets.append(tickets_item)

    result = winningLotteryTicket(tickets)

    fptr.write(str(result) + '\n')

    fptr.close()
