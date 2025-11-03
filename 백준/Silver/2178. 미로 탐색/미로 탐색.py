import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
distance = [[0]*m for _ in range(n)]

def bfs(r,c):
    q = deque([(r,c)])
    visited[r][c] = True
    while q:
        (nr, nc) = q.popleft()
        for dx, dy in dirs:
            x,y = nr+dx, nc+dy
            if 0<=x<n and 0<=y<m and miro[x][y] == 1 and not visited[x][y]:
                distance[x][y] = distance[nr][nc]+1
                q.append((x,y))
                visited[x][y] = True

bfs(0,0)
print(distance[n-1][m-1]+1)