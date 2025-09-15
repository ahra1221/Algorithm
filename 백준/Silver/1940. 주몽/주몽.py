import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
nums = sorted(list(map(int, input().split())))
l = 0
r = n-1
ans = 0
while l < r:
    tmp = nums[l] + nums[r]
    if tmp == m:
        ans += 1
        l += 1
        r -=1
    elif tmp < m:
        l += 1
    else:
        r -=1
print(ans)