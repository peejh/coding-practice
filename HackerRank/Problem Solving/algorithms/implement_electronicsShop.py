# https://www.hackerrank.com/challenges/electronics-shop

#!/bin/python3

import os
import sys
from bisect import bisect_left

def getMoneySpent(keyboards, drives, b):
    '''
    O(n log n) time
    O(1) space
    '''
    
    keyboards = sorted(keyboards)
    drives = sorted(drives)
    max_cost = -1
    
    for k in keyboards:
        diff = b - k

        # take minimum between last index and value of bisect_left
        # in case it returned an index past array length
        i = min(len(drives) - 1, bisect_left(drives, diff))
        
        # check if value at index is greater than difference
        i -= drives[i] > diff # subtracts 1 if TRUE

        # check if cost is still within budget
        # going over can still happen when i is 0 and rolls to -1 in
        # previous statement, which means there are no values less
        # than diff in the drives array
        cost = -1 if k + drives[i] > b else k + drives[i]

        # update max_cost
        max_cost = max(max_cost, cost)
    
    return max_cost


def getMoneySpent_bruteForce(keyboards, drives, b):
    sums = []    
    for k in keyboards:
        for d in drives:
            cost = k + d
            if cost <= b:
                sums.append(cost)

    return max([-1, *sums])


def getMoneySpent_unreadable(keybards, drives, b):
    sums = filter(lambda x: x > 0, [k + d if k + d <= b else 0 for k in keyboards for d in drives])
    
    return max([-1, *sums])    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
