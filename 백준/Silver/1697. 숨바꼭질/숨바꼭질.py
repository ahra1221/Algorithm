from collections import deque


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(distance[x])
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < 100001 and not distance[nx]:
                distance[nx] = distance[x] + 1
                q.append(nx)


n, k = map(int, input().split())
distance = [0] * 100001

bfs()