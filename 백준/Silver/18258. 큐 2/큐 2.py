import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()

for _ in range(N):
    tmp =  sys.stdin.readline().split()
    command = tmp[0]
    if command == 'push':
        q.append(tmp[1])
    if command == 'pop':
        if q:
            print(q.popleft())
        else:
            print("-1")
    if command == 'size':
        print(len(q))
    if command == 'empty':
        if q:
            print("0")
        else:
            print("1")
    if command == 'front':
        if q:
            print(q[0])
        else:
            print("-1")
    if command == 'back':
        if q:
            print(q[-1])
        else:
            print("-1")