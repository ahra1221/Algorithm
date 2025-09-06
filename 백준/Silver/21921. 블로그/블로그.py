import sys

input = sys.stdin.readline
N, X = map(int, input().split())
visitors = list(map(int, input().split()))
window = sum(visitors[:X])
cnt = 1
ans = window

for i in range(X, N):
    window += visitors[i] - visitors[i-X]
    if window > ans:
        ans = window
        cnt = 1
    elif window == ans:
        cnt += 1
if ans > 0:
    print(ans, cnt, sep="\n")
else:
    print("SAD")