import sys

input = sys.stdin.readline
N = int(input())

times = []
for _ in range(N):
    st, en = map(int, input().split())
    times.append((st,en))
times.sort(key=lambda x:(x[1], x[0]))

answer = 0
endtime = 0
for s,e in times:
    if s >= endtime:
        answer += 1
        endtime = e
print(answer)