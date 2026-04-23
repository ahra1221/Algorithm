import sys
from collections import deque

input = sys.stdin.readline
R,C,T = map(int, input().split())
dust = [list(map(int, input().split())) for _ in range(R)]

conditioner = []
for i in range(R):
    if dust[i][0] == -1:
        conditioner.append(i)

#확산
def spread():
    dir = [(1,0),(-1,0),(0,1),(0,-1)]
    spreaded = [[0] * C for _ in range(R)]
    
    for r in range(R):
        for c in range(C):
            if dust[r][c] > 0:
                amount = dust[r][c] // 5
                cnt = 0
                for dx,dy in dir:
                    nx, ny = r + dx, c + dy
                    if 0<=nx<R and 0<=ny<C and dust[nx][ny] != -1:
                        spreaded[nx][ny] += amount
                        cnt += 1
                spreaded[r][c] += dust[r][c] - amount * cnt
    
    for c in conditioner:
        spreaded[c][0] = 0
    return spreaded      
                
#순환
def rotate(grid):
    updir = [(0,1),(-1,0),(0,-1),(1,0)]
    #위쪽
    upx, upy = conditioner[0], 0
    prev = 0
    d = 0
    while d < 4:
        dx, dy = upx + updir[d][0], upy + updir[d][1]
        if dx<0 or dx>conditioner[0] or dy<0 or dy>=C:
            d += 1
            if d == 4: break
            dx, dy = upx + updir[d][0], upy + updir[d][1]
        if grid[dx][dy] >= 0:
            next = grid[dx][dy]
            grid[dx][dy] = prev
            prev = next
        upx, upy = dx,dy
    
    downdir = [(0,1),(1,0),(0,-1),(-1,0)]
    downx,downy = conditioner[1], 0
    prev = 0
    d = 0
    #아래쪽
    while d < 4:
        dx, dy = downx + downdir[d][0], downy + downdir[d][1]
        if dx<conditioner[1] or dx>=R or dy<0 or dy>=C:
            d += 1
            if d == 4: break
            dx, dy = downx + downdir[d][0], downy + downdir[d][1]
        if grid[dx][dy] >= 0:
            next = grid[dx][dy]
            grid[dx][dy] = prev
            prev = next
        downx, downy = dx, dy
    
    for c in conditioner:
        grid[c][0] = 0
    return grid

for _ in range(T):
    dust = rotate(spread())

answer = 0
for r in range(R):
    answer += sum(dust[r])
print(answer)