# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    space = len(f'{number:b}') + 1
    for i in range(1, number+1):
        decimal = f'{i}'.rjust(space-1)
        octal = f'{i:o}'.rjust(space)
        hexadecimal = f'{i:x}'.rjust(space).upper()
        binary = f'{i:b}'.rjust(space)
        print(decimal + octal + hexadecimal + binary)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)