# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem

def wrapper(f):
    def fun(l):
        f(map(lambda n: f'+91 {n[-10:-5]} {n[-5:]}', l))
        # for i, phone_num in enumerate(l):
        #     length = len(phone_num)
        #     stripped = phone_num[length-10:length]
        #     formatted = f'+91 {stripped[:5]} {stripped[5:]}'
        #     l[i] = formatted
        # f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 