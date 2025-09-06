import sys

input = sys.stdin.readline
S = input().strip()
ans = ''
tag = False
word = ''
for s in S:
    if s == "<":
        if word:
            ans += word[::-1]
            word = ''
        ans += s
        tag = True
    elif s == ">":
        ans += s
        tag = False
    elif s == " ":
        if tag:
            ans += s
        else:
            if word:
                ans += word[::-1]
                ans += " "
                word = ''
    elif tag:
        ans += s
    else:
        word += s
if word:
    ans += word[::-1]
print(ans)