import sys

input = sys.stdin.readline
stick = input().strip()
stack = []
ans = 0

for idx, st in enumerate(stick):
    if st == "(":
        stack.append("(")
    else:
        stack.pop()
        if stick[idx-1] == "(":
            ans += len(stack)
        else:
            ans += 1
print(ans)