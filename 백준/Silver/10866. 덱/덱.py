import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
queue = deque()

for _ in range(N):
    command = input().split()
    op = command[0]
    if op == "push_front":
        queue.appendleft(command[1])
    elif op == "push_back":
        queue.append(command[1])
    elif op == "pop_front":
        print(queue.popleft() if queue else -1)
    elif op == "pop_back":
        print(queue.pop() if queue else -1)
    elif op == "size":
        print(len(queue))
    elif op == "empty":
        print(int(not queue))
    elif op == "front":
        print(queue[0] if queue else -1)
    elif op == "back":
        print(queue[-1] if queue else -1)
