import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    q = deque()
    q.extend(list(map(int, input().split())))
    ans = 0

    while M >= 0:
        if q[0] == max(q):
            q.popleft()
            M -= 1
            ans += 1
        else:
            q.append(q.popleft())
            if M == 0:
                M = len(q) - 1
            else:
                M -= 1

    print(ans)