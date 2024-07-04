# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    alpha = list(map(chr, range(97, 123)))
      
    top_lines = list()
    for i in range(1, size+1):
        string = alpha[size-i]
        for j in range(size-i+1, size):
            string = f'{alpha[j]}-{string}-{alpha[j]}'
        top_lines.append(string)
        print(string.center(size*4-3, '-'))
    
    for line in reversed(top_lines[:size-1]):
        print(line.center(size*4-3, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)