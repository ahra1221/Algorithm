import sys
input = sys.stdin.readline
N = int(input())

n = 1
cnt = 1

while n < N:
    n += 6 * cnt
    cnt += 1

print(cnt)