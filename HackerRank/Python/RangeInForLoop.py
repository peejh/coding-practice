# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    T = list()
    for i in range(0,len(string),k):
        curr = set(string[i:i+k])
        for c in curr:
            print(c,end="")
        print()


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)