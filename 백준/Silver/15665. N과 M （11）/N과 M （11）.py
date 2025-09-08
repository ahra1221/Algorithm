import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def backtrace(m, tmp, ans):
    if len(tmp) == m:
        ans.append(tmp.copy())
        return
    prev = None
    for idx, i in enumerate(nums):
        if i == prev:
            continue
        tmp.append(i)
        used[idx] = True

        backtrace(m, tmp, ans)

        tmp.pop()
        used[idx] = False
        prev = i

used = [False] *(N+1)
tmp, ans = [], []
backtrace(M, tmp, ans)

for a in ans:
    print(" ".join(map(str, a)))