import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
board = [[-1] * N for _ in range(N)]
board[0][0] = 1 #뱀

K = int(input())
for _ in range(K):
    r,c = map(int,input().split())
    board[r-1][c-1] = 0 #사과

L = int(input())
dirs = {}
times = deque()
for _ in range(L):
    time, dir = map(str,input().split())
    times.append(int(time))
    dirs[int(time)] = dir

body = deque()
body.append((0,0))
x,y,d = 0,0,0
time = 1
move = [(0,1),(1,0),(0,-1),(-1,0)]

while True:    
    nx,ny = x+move[d][0], y+move[d][1]
    if nx<0 or nx>=N or ny<0 or ny>=N or board[nx][ny] > 0:
        print(time)
        break
    
    body.append((nx,ny))
    if board[nx][ny] != 0: #사과가 없다면
        tailx, taily = body.popleft()
        board[tailx][taily] = -1
    board[nx][ny] = 1
    x, y = nx, ny
    
    if times and time == times[0]:
        t = times.popleft()
        if dirs[t] == "L":
            d = (d-1) % 4
        else:
            d = (d+1) % 4
    
    time += 1 