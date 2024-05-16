import sys

input = sys.stdin.readline

n, m = map(int, input().split())
words = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for _ in range(k):
    sum = 0
    i, j, x, y = map(int, input().split())
    for u in range(i-1, x):
        for w in range(j-1, y):
            sum += words[u][w]
    print(sum)
