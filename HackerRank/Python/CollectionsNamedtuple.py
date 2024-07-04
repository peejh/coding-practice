# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

N = int(input())
Student = namedtuple('Student', input()) # split() not needed
avg = sum([int(Student(*input().split()).MARKS) for _ in range(N)]) / N
print(f"{avg:.2f}")