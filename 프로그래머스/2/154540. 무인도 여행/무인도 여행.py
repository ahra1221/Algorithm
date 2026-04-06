from collections import deque

def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    def bfs(x,y):
        q = deque()
        q.append((x,y))
        visited[x][y] = True
        days = int(maps[x][y])
        while q:
            curx, cury = q.popleft()
            for dx, dy in dirs:
                nx = curx + dx
                ny = cury + dy
                if 0<=nx<n and 0<=ny<m and maps[nx][ny] != "X" and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    days += int(maps[nx][ny])
        return days
    
    for i in range(n):
        for j in range(m):
            if maps[i][j]!= "X" and not visited[i][j]:
                answer.append(bfs(i,j))
    
    return sorted(answer) if answer else [-1]