import sys

input = sys.stdin.readline
N, K = map(int, input().split())
circle = [i for i in range(1, N+1)]
ans = []
tmp = 0

for i in range(N):
    tmp += K-1
    if tmp >= len(circle):
        tmp = tmp % len(circle)
    ans.append(str(circle.pop(tmp)))
    
print("<",", ".join(ans)[:],">", sep='')