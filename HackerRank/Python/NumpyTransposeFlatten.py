# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy as np

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(np.transpose(arr))
print(np.array(arr).flatten())