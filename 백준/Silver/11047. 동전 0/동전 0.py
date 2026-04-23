import sys

input = sys.stdin.readline
N,K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)

answer = 0
idx = 0
while K > 0 and idx < len(coins):
    if (K // coins[idx]) > 0:
        answer += K // coins[idx]
        K %= coins[idx]
    idx += 1

print(answer)