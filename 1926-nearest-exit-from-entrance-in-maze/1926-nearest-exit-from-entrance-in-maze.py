class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n,m = len(maze),len(maze[0])
        sx,sy = entrance[0],entrance[1]

        exits = set()
        for i in [0,n-1]:
            for j in range(m):
                if maze[i][j] == ".":
                    exits.add((i,j))
        
        for i in range(n):
            for j in [0,m-1]:
                if maze[i][j] == ".":
                    exits.add((i,j))
        exits.discard((sx, sy))
        
        if not exits: 
            return -1
        
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = [[False] * m for _ in range(n)]

        answer = -1
        q = deque([(sx,sy,0)])
        visited[sx][sy] = True
        candidate = []
        while q:
            x,y,d = q.popleft()
            if (x,y) in exits:
                answer = d
                break
            for dx,dy in dirs:
                nx,ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and (nx,ny) and not visited[nx][ny] and maze[nx][ny] != "+":
                    q.append((nx,ny,d+1))
                    visited[nx][ny] = True
        return answer