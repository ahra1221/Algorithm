import sys

input = sys.stdin.readline
N,M = map(int, input().split())
bucket = [list(map(int, input().split())) for _ in range(N)]

dirs = [
    # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
    (0,-1), (-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)
]
cross = [
    (-1,-1),(-1,1),(1,-1),(1,1)
]

cloud = {(N-2,0),(N-2,1),(N-1,0),(N-1,1)}

for _ in range(M):
    d,s = map(int, input().split())
    
    dx, dy = dirs[d-1] # 1. 구름 이동
    move_cloud = set()
    for cx, cy in cloud:
        nx = (cx + dx * s) % N
        ny = (cy + dy * s) % N
        move_cloud.add((nx,ny))
    cloud = move_cloud
    
    for x,y in cloud: # 2. 비가 내림
        bucket[x][y] += 1
        
    for x, y in cloud: # 3. 대각선검사
        cnt = 0
        for crossx, crossy in cross:
            i, j = x + crossx, y + crossy
            if 0<=i<N and 0<=j<N:
                if bucket[i][j] > 0: cnt += 1
        bucket[x][y] += cnt
    
    new_cloud = set()   
    for r in range(N):
        for c in range(N):
            if bucket[r][c] >= 2 and (r,c) not in cloud:
                new_cloud.add((r,c))
                bucket[r][c] -= 2
    cloud = new_cloud
    
    # print(bucket)
    # print(cloud)
    # print("-----")

answer = 0
for b in bucket:
    answer += sum(b)
print(answer)