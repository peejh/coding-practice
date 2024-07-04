# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy as np

shape = tuple(map(int, input().split()))
print(np.zeros(shape, dtype='int'))
print(np.ones(shape, dtype='int'))