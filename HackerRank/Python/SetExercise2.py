# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

if __name__ == "__main__":
    A = set(map(int, input().split())) # superset
    n = int(input()) # count of other sets
    res = list()
    for _ in range(n):
        other = set(map(int, input().split())) # other set
        res.append(other.issubset(A))
    
    print(all(res))