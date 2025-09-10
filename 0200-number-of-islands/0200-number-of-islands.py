from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        v = [[False] * c for _ in range(r)]

        def bfs(sr, sc, visited):
            q = deque([(sr,sc)])
            visited[sr][sc] = True
            dirs = [(1,0),(-1,0),(0,1),(0,-1)]
            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if 0<=nr<r and 0<=nc<c and not visited[nr][nc] and grid[nr][nc] == "1":
                        q.append((nr,nc))
                        visited[nr][nc] = True
        ans = 0
        for i in range(r):
            for j in range(c):
                if not v[i][j] and grid[i][j] == "1":
                    bfs(i,j,v)
                    ans += 1

        return ans