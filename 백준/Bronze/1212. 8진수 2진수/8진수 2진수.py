import sys

input = sys.stdin.readline
num = int(input())
num = int(str(num), 8)
print(format(num, 'b'))