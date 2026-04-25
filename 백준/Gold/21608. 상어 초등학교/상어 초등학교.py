import sys

input = sys.stdin.readline
N = int(input())

like = {}
for _ in range(N ** 2):
    inp = list(map(int, input().split()))
    like[inp[0]] = set(inp[1:])

dirs = [(1,0),(-1,0),(0,1),(0,-1)]
seat = [[0] * N for _ in range(N)]

def find_candidate(likes):
    candidate = dict()
    for i in range(N):
        for j in range(N):
            if seat[i][j] == 0: #자리가 비어있음
                near_like = 0
                near_empty = 0
                for dx, dy in dirs: #상하좌우확인
                    nx, ny = i+dx, j+dy
                    if 0<=nx<N and 0<=ny<N:
                        if seat[nx][ny] in likes: #좋아하는 학생이 있음
                            near_like += 1
                        elif seat[nx][ny] == 0:
                            near_empty += 1
                candidate.setdefault(near_like, []).append((near_empty,i, j))
    return candidate

def find_seat(candidate):
    first_key = max(candidate.keys())
    candidate[first_key].sort(key=lambda x: (-x[0], x[1], x[2]))
    i,j = candidate[first_key][0][1], candidate[first_key][0][2]
    return (i,j)

for k, v in like.items():
    x,y = find_seat(find_candidate(v))
    seat[x][y] = k

answer = 0
score = [0, 1, 10, 100, 1000]
#만족도계산
for i in range(N):
    for j in range(N):
        now = seat[i][j]
        nowlike = like[now]
        cnt = 0
        for dx, dy in dirs:
            nx, ny = i+dx, j+dy
            if 0<=nx<N and 0<=ny<N and seat[nx][ny] in nowlike:
                cnt += 1
        answer += score[cnt]

print(answer)