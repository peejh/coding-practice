# https://www.hackerrank.com/challenges/np-polynomials/problem

import numpy as np

P = list(map(float, input().split()))
x = int(input())
print(np.polyval(P, x))

# Numpy functions to perform calculations on Polynomial coefs
# POLY      returns the coefficients of a polynomial with the given sequence of roots
# ROOTS     returns the roots of a polynomial with the given coefficients
# POLYINT   returns an antiderivative (indefinite integral) of a polynomial
# POLYDER   returns the derivative of the specified order of a polynomial
# POLYVAL   evaluates the polynomial at specific value
# POLYFIT   fits a polynomial of a specified order to a set of data using a least-squares approach
# POLYADD
# POLYSUB
# POLYMUL
# POLYDIV