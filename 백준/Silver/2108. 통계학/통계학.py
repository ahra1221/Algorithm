import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]
s = sum(nums)
print(round(s / n))

nums.sort(reverse=True)
print(nums[int(n/2)])

d = dict(Counter(nums))
d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
max_count = d[0][1]
candidate = [k for (k,v) in d if v == max_count]
print(candidate[1] if len(candidate) > 1 else candidate[0])

print(nums[0] - nums[-1])