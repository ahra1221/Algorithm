# 코드를 작성해주세요
import sys 

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

left, right = 0, max(trees)
ans = max(trees)

while left <= right:
    h = 0
    mid = (left+right+1) // 2
    for i in trees:
        if i >= mid:
            h += (i - mid)
    
    if h >= M:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)