import sys
input = sys.stdin.readline
n,k = map(int, input().split())
d = dict()
for _ in range(n):
    t = list(map(int, input().split()))
    con = t[0]
    medal = list(map(int, t[1:]))
    d[con] = medal

d = sorted(d.items(), key=lambda x:(-x[1][0], -x[1][1], -x[1][2]))
rank = 1
for i in range(len(d)):
    if i > 0 and d[i][1] != d[i-1][1]:
        rank = i + 1
    
    if d[i][0] == k:
        print(rank)
        break