from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col for _ in range(row)]
        dirs = ((1,0),(-1,0),(0,1),(0,-1))

        start = None
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    start = (r,c)
                    break
            if start:
                break
        if not start:
            return 0

        q = deque([(r,c)])
        visited[r][c] = True if grid[r][c] else False
        ans = 0
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not (0<=nr<row and 0<=nc<col) or grid[nr][nc] == 0:
                    ans += 1
                else:
                    if not visited[nr][nc]:
                        q.append((nr,nc))
                        visited[nr][nc] = True
        return ans
