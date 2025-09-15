import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
st, en = 0, 0
cur = 0
ans = 0
while True:
    if cur >= m:
        if cur == m:
            ans += 1
        cur -= A[st]
        st += 1
    else:
        if en == n:
            break
        cur += A[en]
        en += 1
print(ans)