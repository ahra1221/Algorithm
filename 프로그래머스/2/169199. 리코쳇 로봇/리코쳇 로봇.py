from collections import deque

def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    visited = [[False] * m for _ in range(n)]
    
    def find_start():
        for i in range(n):
            for j in range(m):
                if board[i][j] == "R":
                    return i, j
    
    def bfs(x,y):
        q = deque()
        q.append((x,y,0))
        visited[x][y] = True
        while q:
            cx,cy,cc = q.popleft()
            
            if board[cx][cy] == "G":
                return cc
            
            #상
            i = cx
            while i-1>=0 and board[i-1][cy] != "D":
                i -= 1
            if not visited[i][cy]:
                q.append((i, cy, cc+1))
                visited[i][cy] = True
            
            #하
            i = cx
            while i+1<n and board[i+1][cy] != "D":
                i += 1
            if not visited[i][cy]:
                q.append((i, cy, cc+1))
                visited[i][cy] = True
            
            #좌
            j = cy
            while j-1>=0 and board[cx][j-1] != "D":
                j -= 1
            if not visited[cx][j]:
                q.append((cx, j, cc+1))
                visited[cx][j] = True
            
            #우
            j = cy
            while j+1<m and board[cx][j+1] != "D":
                j += 1
            if not visited[cx][j]:
                q.append((cx, j, cc+1))
                visited[cx][j] = True
        return -1
    
    stx, sty = find_start()
    
    return bfs(stx,sty)