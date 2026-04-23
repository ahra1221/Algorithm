import sys

input = sys.stdin.readline
N = int(input())
P = list(map(int, input().split()))
P.sort()

answer = 0
prev = 0
for p in P:
    prev += p
    answer += prev
print(answer)