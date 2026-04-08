import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
T = int(input())
grid = [[0] * N for _ in range(N)]
line = 0
ansx, ansy = 0, 0

for i in range(N, 0, -2):
    num = i * i
    
    #down
    for j in range(line, N-line):
        if num == T:
            ansx, ansy = j, line
        grid[j][line] = num
        num -= 1
    
    #right
    for j in range(line+1, N-line):
        if num == T:
            ansx, ansy = N-line-1, j
        grid[N-line-1][j] = num
        num -= 1
    
    #up
    for j in range(N-line-2,line-1,-1):
        if num == T:
            ansx, ansy = j, N-line-1
        grid[j][N-line-1] = num
        num -= 1
        
    #left
    for j in range(N-line-2,line,-1):
        if num == T:
            ansx, ansy = line, j
        grid[line][j] = num
        num -= 1 
    
    line += 1
    
for g in grid:
    print(" ".join(map(str, g)))
print(ansx+1, ansy+1)