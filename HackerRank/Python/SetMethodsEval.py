n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    op = input().split()
    if len(op) == 1:
        eval(f"s.{op[0]}()")
    else:
        eval(f"s.{op[0]}({op[1]})")

print(sum(s))