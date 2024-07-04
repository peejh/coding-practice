# https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy as np

N, M, P = map(int, input().split())
arr1 = np.array([list(map(int, input().split())) for _ in range(N)])
arr2 = np.array([list(map(int, input().split())) for _ in range(M)])
print(np.concatenate((arr1, arr2), axis=0))