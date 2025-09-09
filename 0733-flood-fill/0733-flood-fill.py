from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = [[False] * len(image[0]) for _ in range(len(image))] 
        def bfs(r, c):
            now_color = image[r][c]
            q = deque([(r,c)])
            visited[r][c] = True
            while q:
                r, c = q.popleft()
                dirs = [(1,0),(-1,0),(0,1),(0,-1)]
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0<=nr<len(image) and 0<=nc<len(image[0]):
                        if not visited[nr][nc] and image[nr][nc] == now_color:
                            visited[nr][nc] = True
                            q.append((nr,nc))
        
        bfs(sr,sc)
        for r in range(len(image)):
            for c in range(len(image[0])):
                if visited[r][c]:
                    image[r][c] = color
        return image