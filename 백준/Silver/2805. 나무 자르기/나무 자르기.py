import sys

input = sys.stdin.readline
N,M = map(int, input().split())
trees = list(map(int, input().split()))

st = 0
end = max(trees)
ans = 0

while st <= end:
    mid = (st + end) // 2
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
    
    if total >= M:
        ans = mid
        st = mid + 1
    else:
        end = mid - 1

print(ans)