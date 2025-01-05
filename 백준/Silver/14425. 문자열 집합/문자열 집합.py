n, m = map(int, input().split())
s = set()
s.update(input() for _ in range(n))
ans = 0
for i in range(m):
    tmp = input()
    if tmp in s:
        ans += 1
print(ans)