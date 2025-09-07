import sys

input = sys.stdin.readline
A, B, C, M = map(int, input().split())

tired = 0
work = 0
time = 1

while time <= 24:
    if tired + A <= M:
        work += B
        tired += A
    else:
        tired = max(0, tired - C)
    time += 1
print(work)