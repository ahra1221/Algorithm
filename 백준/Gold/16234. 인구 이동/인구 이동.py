import sys
from collections import deque

input = sys.stdin.readline
N,L,R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dirs = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(i, j):
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    
    union = [(i,j)]
    total = grid[i][j]

    while q:
        x,y = q.popleft()
        for dx, dy in dirs:
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if L <= abs(grid[x][y] - grid[nx][ny]) <= R:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    union.append((nx,ny))
                    total += grid[nx][ny]
    return union,total

answer = 0

while True:
    visited = [[False] * N for _ in range(N)]
    moved = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                u, t = bfs(i, j)
                
                if len(u) > 1:
                    moved = True
                    new = t // len(u)
                    for x, y in u:
                        grid[x][y] = new
    if not moved:
        break
    answer += 1

print(answer)