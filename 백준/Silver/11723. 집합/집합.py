import sys
input = sys.stdin.readline

s = set()
m = int(input())
all_set = set(str(i) for i in range(1, 21))

for _ in range(m):
    c = input().split()
    com = c[0]
    if com == "add":
        s.add(c[1])
    elif com == "remove":
        s.discard(c[1])
    elif com == "check":
        print(1 if c[1] in s else 0)
    elif com == "toggle":
        if c[1] in s:
            s.remove(c[1])
        else:
            s.add(c[1])
    elif com == "all":
        s = all_set.copy()
    elif com == "empty":
        s.clear()