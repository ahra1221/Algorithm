import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
N,M = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(N)]

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(i,j,grid):
    q = deque([(i,j)])
    visited[i][j] = True
    
    while q:
        x,y = q.popleft()
        for dx,dy in dirs:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny] and grid[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    grid[nx][ny] = 2

empty = []
virus = []
for i in range(N):
    for j in range(M):
        if laboratory[i][j] == 0:
            empty.append((i,j))
        elif laboratory[i][j] == 2:
            virus.append((i,j))

answer = 0
for walls in combinations(empty, 3):
    grid = [row[:] for row in laboratory]
    visited = [[False] * M for _ in range(N)]
    
    for wx,wy in walls: grid[wx][wy] = 1
    for vx,vy in virus: bfs(vx,vy,grid)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                cnt += 1
    answer = max(answer, cnt)
print(answer)