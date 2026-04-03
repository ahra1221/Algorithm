class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        
        def dfs(cur):
            visited[cur] = True
            for k in rooms[cur]:
                if not visited[k]:
                    visited[k] = True
                    dfs(k)
        dfs(0)
        return all(visited)