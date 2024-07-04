# https://www.hackerrank.com/contests/projecteuler/challenges/euler011
# Difficulty: EASY

#!/bin/python3

import sys
from operator import mul
from functools import reduce

grid = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)
    
max_hori_prod = 0
for r in range(20):
    for c in range(4, 21):
        prod = reduce(mul, grid[r][c-4:c])
        max_hori_prod = max(max_hori_prod, prod)

max_vert_prod = 0
for c in range(20):
    for r in range(4, 21):
        data = [grid[i][c] for i in range(r-4, r)]
        prod = reduce(mul, data)
        max_vert_prod = max(max_vert_prod, prod)

max_rdiag_prod = 0
for r in range(3, 20):
    for c in range(3, 20):
        data = [grid[r-i][c-i] for i in range(4)]
        prod = reduce(mul, data)
        max_rdiag_prod = max(max_rdiag_prod, prod)

max_ldiag_prod = 0
for r in range(3, 20):
    for c in range(17):
        data = [grid[r-i][c+i] for i in range(4)]
        prod = reduce(mul, data)
        max_ldiag_prod = max(max_ldiag_prod, prod)

print(max(max_hori_prod, max_vert_prod, max_rdiag_prod, max_ldiag_prod))