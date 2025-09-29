import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    s = input().strip()
    print(f"{s[0]}{s[-1]}")