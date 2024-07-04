from collections import Counter

def sol1():
    s = input()
    char_counts = Counter(s)
    chars = sorted(char_counts.keys())
    sorted_chars = sorted(chars, key=char_counts.__getitem__, reverse=True)
    for ch in sorted_chars[:3]:
        print(ch, char_counts[ch])

def sol2():
    s = Counter(sorted(input()))
    for item in s.most_common(3):
        print(*item)

def sol3():
    [print(*item) for item in Counter(sorted(input())).most_common(3)]

if __name__ == '__main__':
    sol1()
    sol2()
    sol3()