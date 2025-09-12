import sys
from collections import Counter

input = sys.stdin.readline
word = list(map(str.lower, input().strip()))
s = Counter(word)
m = max(s.values())
values = [i for i in s if s[i] == m]

if len(values) > 1:
    print("?")
else:
    ans = values.pop()
    print(ans.upper())