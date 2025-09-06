import sys

input = sys.stdin.readline
N, K = map(int, input().split())
nums = list(map(int, input().split()))

st = 0
en = 0
ans = 0
d = {}

while st < N and en < N:
    d[nums[en]] = d.get(nums[en], 0) + 1
    if d[nums[en]] > K:
        while d[nums[en]] > K:
            d[nums[st]] -= 1
            st += 1
    cur = en - st + 1
    if cur > ans:
        ans = cur
    en += 1

print(ans)