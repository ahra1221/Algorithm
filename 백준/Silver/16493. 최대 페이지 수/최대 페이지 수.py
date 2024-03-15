import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[0, 0]] * (M + 1)
dp = [[0] * (N + 1) for _ in range(M + 1)]

for i in range(1, M + 1):
    a, b = map(int, input().split())
    arr[i] = [a, b]

for i in range(1, M + 1):
    day, page = arr[i]
    for j in range(1, N + 1):
        dp[i][j] = dp[i - 1][j]
        if j - day >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - day] + page)

print(dp[M][N])
