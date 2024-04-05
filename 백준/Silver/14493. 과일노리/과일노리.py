import sys

input = sys.stdin.readline

n = int(input())
result = 0

for i in range(n):
    a, b = map(int, input().split())
    mod = result % (a + b)
    if mod < b:
        result += b - mod
    result += 1

print(result)
