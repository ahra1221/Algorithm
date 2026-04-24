import sys

input = sys.stdin.readline
N,M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if map[i][j] == 1: houses.append((i,j))
        elif map[i][j] == 2: chickens.append((i,j))

def cal_distance(house, chicken):
    hx,hy = house
    cx,cy = chicken
    return abs((hx-cx)) + abs((hy-cy))

def chicken_distance(x,y,chicken):
    ans = N*N
    for c in chicken:
        dis = cal_distance((x,y), c)
        ans = min(ans, dis)
    return ans

total_candidate = set()
def dfs(st, cur, chicken):
    if len(cur) == M:
        t = 0
        candidate = []
        for i in cur:
            candidate.append(chicken[i])
        for hx, hy in houses:
            t += chicken_distance(hx,hy, candidate)
        total_candidate.add(t)
        return
    
    for idx in range(st, len(chicken)):
        if idx not in cur:
            cur.append(idx)
            dfs(idx+1, cur, chicken)
            cur.pop()

total = 0
if M == len(chickens):
    for hx, hy in houses:
        total += chicken_distance(hx,hy, chickens)
else:
    dfs(0,[],chickens)
    total = min(total_candidate)

print(total)