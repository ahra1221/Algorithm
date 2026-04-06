from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    dist = [[-1] * m for _ in range(n)]
    dir = [(-1,0),(1,0),(0,-1),(0,1)]
    
    q = deque()
    q.append((0,0))
    dist[0][0] = 1
    while q:
        cur_x, cur_y = q.popleft()
        cur_d = dist[cur_x][cur_y]
        for dx, dy in dir:
            nx, ny = cur_x + dx, cur_y + dy
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny] == 1 and dist[nx][ny] < 0:
                    q.append((nx,ny))
                    dist[nx][ny] = cur_d + 1
    return dist[n-1][m-1]