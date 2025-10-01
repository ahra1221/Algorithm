import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0]
pref = 0
for a in arr:
    pref += a
    prefix.append(pref)
for _ in range(m):
    i, j = map(int, input().split())
    print(prefix[j]-prefix[i-1])