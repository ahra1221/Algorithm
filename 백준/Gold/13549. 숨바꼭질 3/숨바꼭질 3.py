import sys
from collections import deque

input = sys.stdin.readline
N,K = map(int, input().split())

MAX = 100001
INF = 10**9
times = [INF] * (MAX)

q = deque([N])
times[N] = 0
while q:
    cur = q.popleft()
    if cur == K: break
    for x,t in [(cur-1, 1), (cur+1,1), (2*cur,0)]:
        if 0<=x<MAX and  times[x] > times[cur] + t:
            times[x] = times[cur] + t
            q.append(x)
print(times[K])