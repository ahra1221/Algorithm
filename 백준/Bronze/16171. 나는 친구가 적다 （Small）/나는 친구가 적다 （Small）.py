import sys

input = sys.stdin.readline
S = input().strip()
K = input().strip()

tmp = ''
for s in S:
    if not s.isdigit():
        tmp += s
print(int(K in tmp))