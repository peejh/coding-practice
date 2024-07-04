# https://www.hackerrank.com/challenges/find-a-string/

def count_substring(string, sub_string):
    # count = 0
    # for i in range(len(string) - len(sub_string) + 1):
    #     if string[i:].startswith(sub_string):
    #         count += 1
    # return count

    # 1 line version
    return sum(1 for i in range(len(string)-len(sub_string)+1) if string.startswith(sub_string, i))

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)