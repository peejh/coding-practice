from itertools import combinations

def sol1():
    N = int(input())
    arr = input().split()
    K = int(input())

    hit_count = len_combs = 0
    for comb in combinations(arr, K):
        if 'a' in comb:
            hit_count += 1
        len_combs += 1

    print(hit_count / len_combs)

def sol2():
    N, arr, K = int(input()), input().split(), int(input())
    combs = list(combinations(arr, K))
    hit_count = sum(1 for comb in combs if 'a' in comb)
    len_combs = len(combs)
    print(hit_count / len_combs)