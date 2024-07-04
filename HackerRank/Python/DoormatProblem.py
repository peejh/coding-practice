# https://www.hackerrank.com/challenges/designer-door-mat/problem

if __name__ == '__main__':
    N, M = input().split()
    half = int(N) // 2
    M = int(M)
    pattern = ".|."
    welcome = "-WELCOME-"
    
    # print(N, M, half)
    
    for i, n in enumerate(range(half, 0, -1)):
        lines = '---'*n
        print(lines + pattern*(i*2+1) + lines)
    
    print("---"*int((M-9)/6) + welcome + "---"*int((M-9)/6))
    
    for n in range(half):
        lines = '---'*(n+1)
        print(lines + pattern*((half-n-1)*2+1) + lines)