import sys

input = sys.stdin.readline

chess = [input().strip() for _ in range(8)]
cnt = 0

for i in range(8):
    for j in range(0 if i % 2 == 0 else 1, 8, 2):
        k = chess[i][j]
        if k == 'F':
            cnt += 1
        j += 2

print(cnt)
