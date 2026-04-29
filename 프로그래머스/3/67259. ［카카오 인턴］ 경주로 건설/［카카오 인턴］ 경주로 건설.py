from collections import deque

def solution(board):
    
    N = len(board)
    dirs = [(1,0,0),(-1,0,0),(0,1,1),(0,-1,1)]
    INF = float('inf')
    cost = [[[INF] * 2 for _ in range(N)] for _ in range(N)]
    
    q = deque()
    cost[0][0][0] = 0
    cost[0][0][1] = 0
    
    q.append((0,0,0,0))
    q.append((0,0,1,0))
    
    while q:
        x,y,d,c = q.popleft()
        
        for dx,dy,dd in dirs:
            nx,ny,nc = x+dx,y+dy,c+100
            if 0<=nx<N and 0<=ny<N and board[nx][ny] < 1:
                if d != dd: nc += 500
                if nc < cost[nx][ny][dd]:
                    cost[nx][ny][dd] = nc
                    q.append((nx,ny,dd,nc))
    answer = min(cost[N-1][N-1])
    return answer