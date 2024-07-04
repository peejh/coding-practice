# https://www.hackerrank.com/challenges/triangle-quest-2/problem

def sol1():
    for i in range(1, int(input())+1):
        print(*range(1, i+1), *range(i-1, 0, -1), sep='')

# probably fastest; less compute to produce sequence of 1s
def sol2():
    for i in range(1,int(input())+1):
        print(int(ascii(1)*i)**2)

def sol3():
    for i in range(1,int(input())+1):
        print((((10**i)-1)//9)**2)
