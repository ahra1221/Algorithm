import sys

input = sys.stdin.readline
N = int(input())
cur = 1
st = []
ans = []

for i in range(N):
    res = int(input())
    if cur <= res:
        while cur <= res:
            st.append(cur)
            ans.append("+")
            cur += 1
        st.pop()
        ans.append("-")
    else:
        if not st or st[-1] != res:
            ans = []
            break
        else:
            st.pop()
            ans.append("-")

if not ans:
    print("NO")
else:
    print(*ans, sep="\n")