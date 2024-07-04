# https://www.hackerrank.com/challenges/np-linear-algebra/problem

import numpy as np

N = int(input())
matrix = np.array([input().split() for _ in range(N)], dtype='float')
print(np.round(np.linalg.det(matrix), 2))

# Numpy methods to perform Linear Algebra calculations
# LINALG.DET    computes the determinant of an array
# LINALG.EIG    computes the eigenvalues and right eigenvectors of a square array
# LINALG.INV    computes the (multiplicative) inverse of a matrix