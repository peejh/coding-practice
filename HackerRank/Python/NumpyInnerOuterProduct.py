# https://www.hackerrank.com/challenges/np-inner-and-outer/problem

import numpy as np

A = np.array(input().split(), dtype='int')
B = np.array(input().split(), dtype='int')
print(np.inner(A, B))
print(np.outer(A, B))