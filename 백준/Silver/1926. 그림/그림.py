import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dir = [(-1,0),(1,0),(0,-1),(0,1)]
cnt = 0
max_size = 0

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    size = 1
    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in dir:
            next_x = cur_x + dx
            next_y = cur_y + dy
            if 0<=next_x<n and 0<=next_y<m:
                if graph[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    q.append((next_x, next_y))
                    visited[next_x][next_y] = True
                    size += 1
    return size
                    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            size = bfs(i,j)
            max_size = max(max_size, size)
            cnt += 1
print(cnt)
print(max_size)