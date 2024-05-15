import sys

input = sys.stdin.readline

n = int(input())
words = [list(map(int, input().split())) for _ in range(n)]
sum = 0

for i in range(n):
    for j in range(n):
        sum += words[i][j]

print(sum)
