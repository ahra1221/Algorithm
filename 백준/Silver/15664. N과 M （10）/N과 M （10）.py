import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def backtrace(m, tmp, ans, st):
    if len(tmp) == m:
        ans.append(tmp.copy())
        return
    prev = None
    for idx, i in enumerate(nums):
        if used[idx] or i < st:
            continue
        if i == prev:
            continue
        tmp.append(i)
        used[idx] = True
        st = i

        backtrace(m, tmp, ans, st)

        tmp.pop()
        used[idx] = False
        prev = i

used = [False] *(N+1)
tmp, ans = [], []
backtrace(M, tmp, ans, 1)

for a in ans:
    print(" ".join(map(str, a)))