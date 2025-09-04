import sys

input = sys.stdin.readline
S = input().strip()
P = input().strip()
print(1 if P in S else 0)