# https://www.hackerrank.com/challenges/zipped/problem

N, X = map(int, input().split())
subjects = [list(map(float, input().split())) for _ in range(X)]
for subject in zip(*subjects):
    print(sum(subject) / X)