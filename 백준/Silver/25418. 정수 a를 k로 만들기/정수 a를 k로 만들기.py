import sys

input = sys.stdin.readline

A, K = map(int, input().split())
result = 0

while 1:
    if A == K:
        print(result)
        break
    if K % 2 == 0 and K >= A * 2:
        K = int(K / 2)
    else:
        K = K - 1
    result += 1
