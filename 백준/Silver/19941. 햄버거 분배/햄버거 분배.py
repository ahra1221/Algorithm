import sys
input = sys.stdin.readline
n,k = map(int, input().split())
loc = input().strip()
eaten = [False] * n
ans = 0

for i in range(n):
    if loc[i] == "P":
        for j in range(max(0, i-k), min(i+k+1, n)):
            if loc[j] == "H" and not eaten[j]:
                ans += 1
                eaten[j] = True
                break
print(ans)