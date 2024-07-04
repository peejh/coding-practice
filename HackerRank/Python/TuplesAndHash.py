# https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == "__main__":
    n = int(input())
    # t = tuple(map(int, input().split()))
    # t = (*num_list,)
    t = (int(i) for i in input().split())
    print(hash(t))