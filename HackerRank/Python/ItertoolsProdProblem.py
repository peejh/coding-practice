# https://www.hackerrank.com/challenges/maximize-it/problem

from itertools import product

def custom_square(arr):
    arr = list(set(arr))
    return [i**2 for i in arr]

K, M = map(int, input().split())
X = []
for _ in range(K):
    N, *tempX, = map(int, input().split())
    X.append(custom_square(tempX))

mods = [sum(prod) % M for prod in product(*X)]
print(max(mods))