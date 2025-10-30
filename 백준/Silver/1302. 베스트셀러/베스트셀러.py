import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
books = [input().strip() for _ in range(n)]
d = dict(Counter(books))
d = sorted(d.items(), key=lambda x:(-x[1], x[0]))
print(d[0][0])