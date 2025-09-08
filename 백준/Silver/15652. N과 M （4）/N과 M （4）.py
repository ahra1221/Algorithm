import sys
input = sys.stdin.readline
N, M = map(int, input().split())

def backtrace(n, m, tmp, ans, st):
    if len(tmp) == m:
        ans.append(tmp.copy())
        return 
    for i in range(1, n+1):
        if i < st:
            continue
        tmp.append(i)
        used[i] = True
        st = i

        backtrace(n, m, tmp, ans, st)

        tmp.pop()
        used[i] = False

used = [False] * (N+1)
tmp, ans = [], []
backtrace(N, M, tmp, ans, 1)
for a in ans:
    print(" ".join(map(str, a)))