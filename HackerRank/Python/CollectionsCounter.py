# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

if __name__ == "__main__":
    num_of_shoes = int(input())
    size_count = Counter(map(int, input().split()))
    profit = 0
    
    for _ in range(int(input())):
        size, price = map(int, input().split())
        if size_count[size] > 0:
            size_count[size] -= 1
            profit += price
    
    print(profit)