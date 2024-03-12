import sys

input = sys.stdin.readline

n = int(input())

dp = [1 for _ in range(n+1)]

for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2] + 1) % 1000000007

print(dp[n])
