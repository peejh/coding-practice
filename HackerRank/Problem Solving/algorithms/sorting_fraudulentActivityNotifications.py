# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/

#!/bin/python3

from bisect import bisect, insort
import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    notif_count = 0
    for i in range(d, len(expenditure)):
        exp = expenditure[i]
        median = getMedian(expenditure[i-d:i])
        if exp >= median * 2:
            notif_count += 1
    return notif_count
        
def getMedian(arr):
    length = len(arr)
    arr.sort()
    mid = length // 2
    if length % 2:
        return arr[mid]
    else:
        return (arr[mid] + arr[mid-1]) / 2

def activityNotifications(expenditure, d):
    notif_count = 0
    trail = sorted(expenditure[:d])
    
    for i in range(d, len(expenditure)):
        # print(trail)
        curr_exp = expenditure[i]   # defining for readability
        edge_exp = expenditure[i-d] # defining for readability
        median = getMedianFromSorted(trail)        
        # print("curr_exp = ", curr_exp, "edge_exp = ", edge_exp)
        
        if curr_exp >= median * 2:
            notif_count += 1
            
        # reprocess the trail
        idx_edge = bisect(trail, edge_exp) # returns position, not index
        trail.pop(idx_edge-1)
        insort(trail, curr_exp)
        
    return notif_count
        
def getMedianFromSorted(sorted_arr):
    length = len(sorted_arr)
    mid = length // 2
    if length % 2:
        return sorted_arr[mid]
    else:
        return (sorted_arr[mid] + sorted_arr[mid-1]) / 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
