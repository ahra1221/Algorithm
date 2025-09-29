import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

st = 0
en = len(arr)-1
ans = 0

while st < en:
    s = arr[st] + arr[en]
    if s < x:
        st += 1
    elif s > x:
        en -= 1
    else:
        st += 1
        en -= 1
        ans += 1
print(ans)
