import sys

input = sys.stdin.readline
N = int(input())
schedule = []
for _ in range(N):
    t,p = map(int, input().split())
    schedule.append((t,p))

dp = [0] * (N+1)
dp[0] = 0
for i in range(N):
    if i + 1 <= N:
        dp[i+1] = max(dp[i], dp[i+1])
    t,p = schedule[i]
    if i+t <= N:
        dp[i+t] = max(dp[i+t], dp[i] + p)

print(dp[-1])
        