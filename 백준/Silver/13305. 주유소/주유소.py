import sys

input = sys.stdin.readline
N = int(input())
road = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

price = oil_price[0]
answer = road[0] * price
for i in range(1, N-1):
    if oil_price[i] < price:
        price = oil_price[i]
    answer += price * road[i]
print(answer)