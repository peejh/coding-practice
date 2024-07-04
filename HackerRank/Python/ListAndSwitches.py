# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    nums = list()
    
    # new
    # for _ in range(N):
    #     command = input().split()
    #     # print(command)
    #     match (command[0]):
    #         case 'insert':
    #             idx, num = map(int, [command[1], command[2]])
    #             nums.insert(idx, num)
    #         case 'print':
    #             print(nums)
    #         case 'remove':
    #             num = int(command[1])
    #             nums.remove(num)
    #         case 'append':
    #             num = int(command[1])
    #             nums.append(num)
    #         case 'sort':
    #             nums.sort()
    #         case 'pop':
    #             if (nums):
    #                 nums.pop()
    #         case 'reverse':
    #             nums.reverse()

    funcs = {
        'insert': lambda args: nums.insert(int(args[1]), int(args[2])),
        'print': lambda args: print(nums),
        'remove': lambda args: nums.remove(int(args[1])),
        'append': lambda args: nums.append(int(args[1])),
        'sort': lambda args: nums.sort(),
        'pop': lambda args: nums.pop(),
        'reverse': lambda args: nums.reverse()
    }

    for _ in range(N):
        command = input().split()
        funcs[command[0]](command)
