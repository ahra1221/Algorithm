import sys
from collections import defaultdict
input = sys.stdin.readline
n,k = map(int, input().split())
A = list(map(int, input().split()))

pref = 0
freq = defaultdict(int)
freq[0] = 1
ans = 0

for x in A:
    pref += x
    ans += freq[pref-k]
    freq[pref] += 1

print(ans)