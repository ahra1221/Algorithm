import sys

input = sys.stdin.readline
n = int(input())
x = list(map(int, input().split()))
sorted_x = sorted(list(set(x)))
d = dict()
for idx, n in enumerate(sorted_x):
    d[n] = idx
ans = []
for n in x:
    ans.append(d[n])
print(" ".join(map(str, ans)))