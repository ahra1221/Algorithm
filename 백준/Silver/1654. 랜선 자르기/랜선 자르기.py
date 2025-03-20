# 코드를 작성해주세요
K, N = map(int, input().split())
lenson = [int(input()) for _ in range(K)]

left, right = 0, max(lenson)
ans = max(lenson)

while left <= right:
    cnt = 0
    mid = (left+right+1) // 2
    for i in lenson:
        cnt += i // mid
    if cnt >= N:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
        
print(ans)