from textwrap import wrap

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print(uniqfy(string[i:i+k]))

def uniqfy(string):
    res = []
    for ch in string:
        if ch not in res:
            res.append(ch)
    return res

# leverages preservation of insert order of keys
# in a dictionary; not true in older python versions
def merge_the_tools_2(string, k):
    for i in range(0, len(string), k):
        print(''.join(dict.fromkeys(string[i:i+k])))

# uses wrap
def merge_the_tools_3(string, k):
    for item in wrap(string, k):
        temp_set = list(set(item))
        temp_set.sort(key=lambda x: item.index(x))
        print("".join(temp_set))

# one line version
def merge_the_tools_4(string, k):
	print(*map(lambda x: "".join(sorted(set(x), key=x.index)), wrap(string, k)), sep="\n")

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)