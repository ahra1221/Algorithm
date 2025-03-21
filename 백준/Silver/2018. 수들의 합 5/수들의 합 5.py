N = int(input())
sum = 0
en = 0
cnt = 0

for st in range(0, N):
    while sum < N and en< N:
        sum += (en+1)
        en += 1
    if sum == N:
        cnt += 1
    sum -= (st+1)

print(cnt)
        
