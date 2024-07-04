# https://www.hackerrank.com/challenges/ginorts/problem

def sort_key(x):
    if x.islower():
        return 1
    elif x.isupper():
        return 2
    elif x.isdigit() and int(x) % 2 == 1:
        return 3
    elif x.isdigit() and int(x) % 2 == 0:
        return 4
    return 5

S = sorted(input())
print(''.join(sorted(S, key=sort_key)))