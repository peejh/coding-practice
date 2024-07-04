# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

S, k = input().split()
for i in range(1, int(k)+1):
    combs = [''.join(list(elem)) for elem in combinations(sorted(S), i)]
    print(*combs, sep='\n')