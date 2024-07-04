# https://www.hackerrank.com/challenges/py-the-captains-room/problem

from collections import Counter

# by frequency analysis
def sol1():
    K = int(input())
    rooms = Counter(map(int, input().split()))
    for k, v in rooms.items():
        if v == 1:
            print(k)
            break

# mathematical solution
def sol2():
    K = int(input())
    rooms = list(map(int, input().split()))
    uniq_rooms = set(rooms)
    captains_room = ((sum(uniq_rooms) * K) - sum(rooms)) // (K - 1)
    print(captains_room)