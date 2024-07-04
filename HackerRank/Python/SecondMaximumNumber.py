# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    uniq_scores = list(set(arr))
    uniq_scores.sort()
    print(uniq_scores[-2])