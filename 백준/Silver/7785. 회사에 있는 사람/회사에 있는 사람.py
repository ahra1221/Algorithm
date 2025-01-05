n = int(input())
s = set()
for _ in range(n):
    i, j = input().split()
    if j == "enter":
        s.add(i)
    else:
        s.remove(i)
s = sorted(s, reverse=True)
for i in s: print(i)