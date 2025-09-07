import sys
from collections import deque

input = sys.stdin.readline
N,M,V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")
    for v in sorted(graph[start]):
        if not visited[v]:
            dfs(graph, v, visited)

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in sorted(graph[v]):
            if not visited[i]:
                q.append(i)
                visited[i] = True 

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)