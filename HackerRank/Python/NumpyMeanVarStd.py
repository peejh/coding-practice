# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy as np

N, M = map(int, input().split())
arr = np.array([input().split() for _ in range(N)], dtype='float')
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(np.around(np.std(arr), 11))