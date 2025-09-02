import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
queue = deque()
queue.extend(range(1, N+1))

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue.popleft())