import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
loc = sorted(list(map(int, input().split())))

first = loc[0]
last = n - loc[-1]
mid = 0

for a, b in zip(loc, loc[1:]):
    gap = b-a
    mid = max((gap+1) // 2, mid)

print(max(first, mid, last))