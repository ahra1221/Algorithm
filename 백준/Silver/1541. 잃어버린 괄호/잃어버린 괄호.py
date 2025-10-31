import sys

input = sys.stdin.readline
s = input().strip()
parts = s.split('-')
ans = sum(map(int, parts[0].split('+')))
for p in parts[1:]:
    ans -= sum(map(int, p.split('+')))
print(ans)