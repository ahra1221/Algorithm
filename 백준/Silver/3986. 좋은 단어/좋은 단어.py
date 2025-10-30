import sys

input = sys.stdin.readline
n = int(input())
ans = 0

for _ in range(n):
    word = list(input().strip())
    st = []
    for w in word:
        if st:
            if st[-1] == w:
                st.pop()
            else:
                st.append(w)
        else:
            st.append(w)
    ans += 1 if not st else 0
print(ans)