# https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy as np

N, M = map(int, input().split())
arr1 = np.array([list(map(int, input().split())) for _ in range(N)])
arr2 = np.array([list(map(int, input().split())) for _ in range(N)])
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 // arr2) # floor divide
print(arr1 % arr2)
print(arr1 ** arr2)