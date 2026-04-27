import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

size = 2
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
eat = 0

baby = (0,0)
for i in range(N):
    for j in range(N):
        val = grid[i][j]
        if val == 9:
            baby = (i,j)
            grid[i][j] = 0
            break

def bfs(i,j):
    q = deque([(i,j,0)])
    visited = [[False] * N for _ in range(N)]
    visited[i][j] = True
    candidates = []
    min_dist = -1
    
    while q:
        x,y,dist = q.popleft()
        
        if min_dist != -1 and dist > min_dist:
            break
        
        if 0 < grid[x][y] < size:
            min_dist = dist
            candidates.append((dist, x, y))
            continue
        
        for dx,dy in dirs:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and grid[nx][ny] <= size and not visited[nx][ny]:
                q.append((nx,ny,dist+1))
                visited[nx][ny] = True
    
    if not candidates:
        return None
    candidates.sort()
    return candidates[0]

time = 0
while True:
    res = bfs(baby[0],baby[1])
    if res is None: break
    
    t, fx, fy = res
    fs = grid[fx][fy]
        
    time += t
    eat += 1
    if eat == size:
        eat = 0
        size += 1
    
    grid[baby[0]][baby[1]] = 0
    grid[fx][fy] = 0
    baby = (fx,fy)

print(time)