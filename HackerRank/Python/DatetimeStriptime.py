# https://www.hackerrank.com/challenges/python-time-delta/problem

import os
from datetime import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    tformat = '%a %d %b %Y %H:%M:%S %z'
    tdiff = dt.strptime(t1, tformat) - dt.strptime(t2, tformat)
    return f'{abs(tdiff.total_seconds()):.0f}'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()