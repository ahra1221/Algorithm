import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
queue = deque()

for _ in range(N):
    command = input().split()
    op = command[0]
    if op == "front":
        print(queue[0] if queue else -1)
    elif op == "back":
        print(queue[-1] if queue else -1)
    elif op == "empty":
        print(int(not queue))
    elif op == "size":
        print(len(queue))
    elif op == "pop":
        print(queue.popleft()) if queue else print(-1)
    else:
        queue.append(command[1])