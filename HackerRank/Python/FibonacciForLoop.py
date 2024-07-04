# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true

cube = lambda x: x**3

def fibonacci(n):
    if n == 0:
        return []
    
    fibseq = list()    
    for i in range(n):
        if (i < 2):
            fibseq.append(i)
        else:
            prev = fibseq[i-1]
            prevprev = fibseq[i-2]
            fibseq.append(prev + prevprev)
    
    return fibseq

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))