import sys
from collections import Counter
input = sys.stdin.readline

n,c = map(int, input().split())
nums = list(map(int, input().split()))
order = {}
cnt = dict(Counter(nums))

for idx, n in enumerate(nums):
    if not n in order:
        order[n] = idx
tmp = {k: (cnt[k],order[k]) for k in cnt.keys()}
ans = sorted(tmp.items(), key = lambda x: (-x[1][0],x[1][1]))
result = ""
result = " ".join(str(a) for a, b in ans for _ in range(b[0]))
print(result)