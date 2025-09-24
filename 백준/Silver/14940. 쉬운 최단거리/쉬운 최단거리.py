import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dis = [[0] * m for _ in range(n)]

sr = sc = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dis[i][j] = -1
        elif graph[i][j] == 2:
            sr, sc = i, j 

def bfs(r, c):
    q = deque()
    q.append((r,c))
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        sr, sc = q.popleft()
        for dr, dc in directions:
            nr, nc = sr + dr, sc + dc
            if (0<=nr<n) and (0<=nc<m):
                if graph[nr][nc] == 1 and dis[nr][nc] == -1:
                    dis[nr][nc] = dis[sr][sc] + 1
                    q.append((nr, nc))

bfs(sr, sc)

for i in range(n):
    print(*dis[i])