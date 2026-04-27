import sys
from collections import deque

input = sys.stdin.readline
N,M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(i,j):
    q = deque([(i,j)])
    visited = [[False] * M for _ in range(N)]
    visited[i][j] = True
    melt = set()
    
    while q:
        x,y = q.popleft()
        for dx,dy in dirs:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and  not visited[nx][ny]:
                visited[nx][ny] = True
                if cheese[nx][ny] == 0:
                    q.append((nx,ny))
                elif cheese[nx][ny] == 1:
                    melt.add((nx,ny))
    return melt

time = 0
last = 0
while True:
    melt = bfs(0,0)
    if not melt: break
    
    for x, y in melt:
        cheese[x][y] = 0
    last = len(melt)
    time += 1

print(time)
print(last)