import sys
input = sys.stdin.readline
n = int(input())
sol = sorted(list(map(int, input().split())))
st = 0
en = n-1
ans = (sol[st], sol[en])
cur = float('inf')

while st < en:
    tmp = sol[st] + sol[en]
    if abs(tmp) < cur:
        cur = abs(tmp)
        ans = [sol[st],sol[en]]
        if tmp == 0:
            break
    if tmp < 0 :
        st += 1
    else:
        en -= 1
print(" ".join(map(str, ans)))
    