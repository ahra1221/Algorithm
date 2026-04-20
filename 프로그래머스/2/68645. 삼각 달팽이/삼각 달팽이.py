def solution(n):
    answer = []
    target = 0
    for i in range(1,n+1):
        target += i
        
    
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    
    snail = [[0] * n for _ in range(n)]
    nx,ny = 0,0
    
    num = 1
    snail[0][0] = num
    dir = 0
    while (num <= target):
        snail[nx][ny] = num
        nextx, nexty = nx+dx[dir],ny+dy[dir]
        if(nextx < 0 or nextx >= n or nexty <0 or nexty >= n or snail[nextx][nexty] > 0):
            dir = (dir + 1) % 3
            nextx, nexty = nx+dx[dir],ny+dy[dir]
        
        nx = nextx
        ny = nexty
        num += 1
    
    for i in range(n):
        for j in range(i+1):
            answer.append(snail[i][j])
    
    return answer