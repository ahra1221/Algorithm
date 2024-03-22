import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q.append([x, y])
    c = [[0] * m for _ in range(n)]
    c[x][y] = 1
    num = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if map[nx][ny] == 'L' and c[nx][ny] == 0:
                    c[nx][ny] = c[x][y] + 1
                    num = max(num, c[nx][ny])
                    q.append([nx, ny])
    return num - 1


n, m = map(int, input().split())
map = [list(map(str, input())) for _ in range(n)]
q = deque()

cnt = 0
for i in range(n):
    for j in range(m):
        if map[i][j] == 'L':
            cnt = max(cnt, bfs(i, j))
print(cnt)
