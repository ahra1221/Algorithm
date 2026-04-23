import sys

input = sys.stdin.readline
N = int(input())
power = [list(map(int, input().split())) for _ in range(N)]
answer = 1000

def cal(team):
    total = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            a = team[i]
            b = team[j]
            total += power[a][b] + power[b][a]
    return total

def dfs(st,cur):
    global answer
    if len(cur) == N / 2:
        link = [i for i in range(N) if i not in cur]
        diff = abs(cal(cur) - cal(link))
        answer = min(answer, diff)
        return

    for i in range(st, N):
        if i not in cur:
            cur.append(i)
            dfs(i+1,cur)
            cur.pop()

dfs(1,[0])
print(answer)
 