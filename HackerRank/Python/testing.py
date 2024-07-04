import sys

print(sys.getsizeof([1, 2, 3]))
print(sys.getsizeof("1 2 3"))
print(sys.getsizeof(True))

x = tuple(3)
print(x)