import sys
input = sys.stdin.readline

n = int(input())
locals = list(map(int, input().split()))
m = int(input())

l,r = 0, max(locals)
if sum(locals) <= m:
    print(r)
    sys.exit(0)

ans = 0
while l <= r:
    mid = (l+r) // 2
    total = 0
    for x in locals:
        if x <= mid:
            total += x
        else:
            total += mid
    if total <= m:
        ans = mid
        l = mid + 1 
    else:
        r = mid - 1
print(ans)