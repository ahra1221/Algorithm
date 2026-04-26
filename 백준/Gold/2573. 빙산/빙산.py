import sys
from collections import deque

input = sys.stdin.readline
N,M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(sx,sy):
    q = deque([(sx,sy)])
    visited[sx][sy] = True
    
    while q:
        x,y = q.popleft()
        for dx,dy in dirs:
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and ice[nx][ny] > 0:
                q.append((nx,ny))
                visited[nx][ny] = True
  
answer = 0       
while True:
    visited = [[False] * M for _ in range(N)]
    island = 0
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and ice[i][j] > 0:
                bfs(i, j)
                island += 1
                
    if island >= 2:
        print(answer)
        break

    if island == 0:
        print(0)
        break
    
    #녹이기
    after = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ice[i][j] == 0: continue
            sea = 0
            for dx,dy in dirs:
                nx,ny = i+dx, j+dy
                if 0<=nx<N and 0<=ny<M and ice[nx][ny] == 0:
                    sea += 1
            after[i][j] = max(0,ice[i][j] - sea)
    
    ice = after
    answer += 1    