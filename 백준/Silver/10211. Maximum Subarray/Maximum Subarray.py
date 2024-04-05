import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * num
    dp[0] = arr[0]
    for i in range(1, num):
        dp[i] = max(dp[i-1] + arr[i], arr[i])
    print(max(dp))

