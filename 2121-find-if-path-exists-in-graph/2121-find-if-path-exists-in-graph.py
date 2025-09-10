from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True
        graph = [[] for _ in range(n)]
        visited = [False] * n
        for ed in edges:
            graph[ed[0]].append(ed[1])
            graph[ed[1]].append(ed[0])
        print(graph)
        def bfs(s, d):
            q = deque([s])
            visited[s] = True
            while q:
                v = q.popleft()
                for i in graph[v]:
                    if not visited[i]:
                        q.append(i)
                        visited[i] = True
                    if i == d:
                        return True
            return False
        return bfs(source, destination)
            