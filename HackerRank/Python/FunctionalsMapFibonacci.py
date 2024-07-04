# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    res = [0, 1]
    for i in range(2, n):
        next_fib = res[i-1] + res[i-2]
        res.append(next_fib)
    return res[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))