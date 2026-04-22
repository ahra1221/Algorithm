import sys

input = sys.stdin.readline
N,M = map(int,input().split())
fuel = [list(map(int, input().split())) for _ in range(N)]

INF = int(1e9)
dp = [[[INF] * 3 for _ in range(M)] for _ in range(N)]

for y in range(M):
    for d in range(3):
        dp[0][y][d] = fuel[0][y]

for x in range(1, N):
    for y in range(M):
        f = fuel[x][y]
        if y - 1 >= 0:
            dp[x][y][0] = f + min(dp[x-1][y-1][1], dp[x-1][y-1][2])
        
        dp[x][y][1] = f + min(dp[x-1][y][0], dp[x-1][y][2])
        
        if y + 1 < M:
            dp[x][y][2] = f + min(dp[x-1][y+1][0], dp[x-1][y+1][1])

ans = INF
for y in range(M):
    ans = min(ans, min(dp[N-1][y]))

print(ans)