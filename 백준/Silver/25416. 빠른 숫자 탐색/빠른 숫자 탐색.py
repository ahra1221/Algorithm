from collections import deque
import sys

input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

graph = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
visited = [[False] * 5 for _ in range(5)]


def bfs(y, x):
    q = deque([(y, x, 0)])
    visited[y][x] = True
    while q:
        y, x, cnt = q.popleft()
        if graph[y][x] == 1:
            return cnt
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5:
                if not visited[ny][nx] and graph[ny][nx] != -1:
                    visited[ny][nx] = True
                    q.append((ny, nx, cnt + 1))
    return -1


print(bfs(r, c))