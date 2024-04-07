import sys

input = sys.stdin.readline
bag = [[0,0]]

N, K = map(int, input().split())
result = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    W, V = map(int, input().split())
    bag.append([W, V])

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = bag[i][0]
        value = bag[i][1]
        if j < weight:
            result[i][j] = result[i - 1][j]
        else:
            result[i][j] = max(value + result[i - 1][j - weight], result[i - 1][j])

print(result[N][K])


