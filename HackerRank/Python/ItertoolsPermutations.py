# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

if __name__ == "__main__":
    text, k = input().split()
    out = [''.join(item) for item in permutations(text, int(k))]
    print('\n'.join(sorted(out)))

    # # ver 2
    # text, k = input().split()
    # out = [''.join(item) for item in permutations(sorted(text), int(k))]
    # print('\n'.join(out))

    # # ver 3
    # text, k = input().split()
    # out = permutations(sorted(text), int(k))
    # for permutation in out:
    #     print(''.join(permutation))