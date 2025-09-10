from collections import deque
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        visited = [[False] * cols for _ in range(rows)] 
        ans = []
        q = deque([(rCenter, cCenter)])
        visited[rCenter][cCenter] = True
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c = q.popleft()
            ans.append((r,c))
            for dr, dc in dirs:
                nr,nc = r+dr ,c+dc
                if 0<=nr<rows and 0<=nc<cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr,nc))
        return ans
            
