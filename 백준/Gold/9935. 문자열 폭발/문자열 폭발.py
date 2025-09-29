import sys
input = sys.stdin.readline
s = input().strip()
bomb = input().strip()

m = len(bomb)
last = bomb[-1]
st = []

for ch in s:
    st.append(ch)
    if ch == last and len(st) >= m and st[-m:] == list(bomb):
        del st[-m:]
print("".join(st) if st else "FRULA")