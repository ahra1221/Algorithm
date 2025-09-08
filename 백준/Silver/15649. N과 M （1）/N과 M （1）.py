import sys
N, M = map(int, input().split())

def backtrack(n, m, used, tmp, ans):
    if len(tmp) == m:
        ans.append(tmp.copy())
        return
    for i in range(1,n+1):
        if used[i]:
            continue
        tmp.append(i)
        used[i] = True
        backtrack(n, m, used, tmp, ans)
        tmp.pop()
        used[i] = False

used = [False] * (N+1)
ans = []
tmp = []
backtrack(N, M, used, tmp, ans)
for a in ans:
    print(" ".join(map(str, a)))