import sys

input = sys.stdin.readline
N = int(input())
cows = [-1] * 10
ans = 0

for _ in range(N):
    num, road = map(int, input().split())
    tmp = cows[num-1]
    if tmp != road and tmp > -1:
        ans += 1
    cows[num-1] = road
print(ans)