# https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy as np

numbers = list(map(int, input().split()))
print(np.reshape(numbers, (3, 3)))