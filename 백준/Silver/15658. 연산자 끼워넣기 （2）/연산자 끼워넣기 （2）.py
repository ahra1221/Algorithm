import sys

input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

max_ans = -1000000001
min_ans = 1000000001


def dfs(idx, ans):
    global max_ans, min_ans

    if idx == N:
        max_ans = max(max_ans, ans)
        min_ans = min(min_ans, ans)
        return

    if op[0] > 0:
        op[0] -= 1
        dfs(idx + 1, ans + num[idx])
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        dfs(idx + 1, ans - num[idx])
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        dfs(idx + 1, ans * num[idx])
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        dfs(idx + 1, int(ans/num[idx]))
        op[3] += 1


dfs(1, num[0])
print(max_ans)
print(min_ans)
