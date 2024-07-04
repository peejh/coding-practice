# https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy as np
# from functools import reduce

N, M = map(int, input().split())
arr = np.array([input().split() for _ in range(N)], dtype='int')
# print(reduce(lambda x, y: x*y, np.sum(arr, axis=0)))
print(np.prod(np.sum(arr, axis=0)))