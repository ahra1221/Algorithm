import sys

input = sys.stdin.readline
N, M = map(int, input().split())
lights = list(map(int, input().split()))

for idx in range(M):
    command = list(map(int, input().split()))
    op = command[0]
    l = command[1]
    r = command[2]
    if op == 1:
        lights[l-1] = r
    elif op == 2:
        for i in range(l-1,r):
            lights[i] = int(not bool(lights[i]))
    elif op == 3:
        for i in range(l-1,r):
            lights[i] = 0
    elif op == 4:
        for i in range(l-1,r):
            lights[i] = 1 

print(*lights)