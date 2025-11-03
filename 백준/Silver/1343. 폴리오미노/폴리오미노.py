import sys

input = sys.stdin.readline
board = input().strip()
ans = ""
cnt = 0
for ch in board:
    if ch == "X":
        cnt += 1
    else:
        if cnt % 2 == 1:
            print(-1)
            sys.exit(0)
        ans += "AAAA" * (cnt // 4) + "BB" * ((cnt % 4) // 2)
        ans += "."
        cnt = 0
if cnt % 2 == 1:
    print(-1)
    sys.exit(0)
ans += "AAAA" * (cnt // 4) + "BB" * ((cnt % 4) // 2)
print(ans)