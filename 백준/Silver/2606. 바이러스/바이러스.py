import sys

input = sys.stdin.readline
computer = int(input())
N = int(input())
graph = [[] for _ in range(computer+1)]
vistied = [False] * (computer+1)

for _ in range(N):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(gr, st, v):
    v[st] = True
    for g in gr[st]:
        if not v[g]:
            dfs(gr, g, v)
            
    
dfs(graph, 1, vistied)
print(sum(vistied)-1)