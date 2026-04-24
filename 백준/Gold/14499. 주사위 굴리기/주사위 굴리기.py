import sys

input = sys.stdin.readline
N,M,x,y,K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

# 0: 위, 1: 아래, 2: 북, 3: 남, 4: 동, 5: 서
dice = [0, 0, 0, 0, 0, 0]

dirs = {
    1: (0,1),
    2: (0,-1),
    3: (-1,0),
    4: (1,0)
}

def roll(d):
    global dice
    if d == 1: #동쪽
        dice[0], dice[1], dice[4],dice[5] = dice[5], dice[4], dice[0], dice[1]
    elif d == 2: #서쪽
        dice[0], dice[1], dice[4],dice[5] = dice[4], dice[5], dice[1], dice[0]
    elif d == 3: #북쪽
        dice[0], dice[1], dice[2],dice[3] = dice[3], dice[2], dice[0], dice[1]
    else: #남쪽
        dice[0], dice[1], dice[2],dice[3] = dice[2], dice[3], dice[1], dice[0]

underx, undery = 1, 2

for com in command:
    dx,dy = dirs[com]
    nx,ny = x + dx, y + dy
    if 0<=nx<N and 0<=ny<M:
        #주사위굴리기
        roll(com)
        x, y = nx, ny
        if grid[x][y] == 0:
            grid[x][y] = dice[1]
        else:
            dice[1] = grid[x][y]
            grid[x][y] = 0
        print(dice[0])
    else:
        continue
        