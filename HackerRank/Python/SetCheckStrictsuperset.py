def sol1():
    A = set(map(int, input().split()))
    res = []
    for _ in range(int(input())):
        other = set(map(int, input().split()))
        res.append(A.issuperset(other))
    print(all(res))

def sol2():
    A = set(map(int, input().split()))
    flag = True
    for _ in range(int(input())):
        other = set(map(int, input().split()))
        if not A.issuperset(other):
            flag = False
            break
    print(flag)

def sol3():
    A = set(input().split())
    N = int(input())
    res = [A.issuperset(set(input().split())) for _ in range(N)]
    print(all(res))