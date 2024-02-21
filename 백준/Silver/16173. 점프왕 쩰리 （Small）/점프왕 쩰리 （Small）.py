from collections import deque

n = int(input())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

visited = []
for _ in range(n):
    visited.append([False]*n)

dx = [1, 0]
dy = [0, 1]


def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        if array[x][y] == -1:
            return 'HaruHaru'
        for i in range(2):
            nx = x + dx[i] * array[x][y]
            ny = y + dy[i] * array[x][y]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] == True:
                continue
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return 'Hing'


print(bfs(0, 0, visited))