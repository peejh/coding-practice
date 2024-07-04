# https://www.hackerrank.com/challenges/polar-coordinates/problem

from cmath import phase
from cmath import sqrt

z = complex(input())
x = z.real
y = z.imag
print(abs(sqrt(x**2 + y**2)))
print(phase(z))