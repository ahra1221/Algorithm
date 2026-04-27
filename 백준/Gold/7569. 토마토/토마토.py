import sys
from collections import deque

input = sys.stdin.readline
M,N,H = map(int, input().split())

tomato = []
for _ in range(H):
    l = [list(map(int, input().split())) for _ in range(N)]
    tomato.append(l)

dirs = [(0,0,1),(0,0,-1),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0)]

q = deque()
for z in range(H):
    for x in range(N):
        for y in range(M):
            if tomato[z][x][y] == 1:
                q.append((z, x, y))
                
while q:
    z, x,y = q.popleft()
        
    for dz, dx,dy in dirs:
        nz,nx,ny=  z+dz, x+dx, y+dy
        if 0<=nx<N and 0<=ny<M and 0<=nz<H and tomato[nz][nx][ny] == 0:
                tomato[nz][nx][ny] = tomato[z][x][y] + 1
                q.append((nz,nx,ny))

answer = 0
for z in range(H):
    for x in range(N):
        for y in range(M):
            if tomato[z][x][y] == 0:
                print(-1)
                sys.exit()
            answer = max(answer, tomato[z][x][y])

print(answer -1)
                