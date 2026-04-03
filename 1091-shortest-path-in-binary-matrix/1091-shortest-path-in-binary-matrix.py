class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ans = -1
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return ans

        visited = [[False] * n for _ in range(n)]
        dxy = [
            (-1,0),(1,0),(0,-1),(0,1),
            (-1,-1),(-1,1),(1,-1),(1,1)
        ]

        queue = deque()
        queue.append((0,0,1))
        visited[0][0] = True
        while queue:
            curx, cury, curl = queue.popleft()

            if curx == n-1 and cury == n-1:
                ans = curl
                break

            for dx, dy in dxy:
                nextx,nexty = curx+dx, cury+dy
                if nextx >= 0 and nextx < n and nexty >= 0 and nexty < n:
                    if grid[nextx][nexty] == 0 and not visited[nextx][nexty]:
                        visited[nextx][nexty] = True
                        queue.append((nextx,nexty,curl+1))
        return ans