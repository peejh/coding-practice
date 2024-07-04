if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    elems = sorted(list(arr), reverse=True)
    high = max(elems)
    for i in range(len(elems)):
        if (elems[i] < high):
            print(elems[i])
            break