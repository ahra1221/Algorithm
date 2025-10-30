import sys

input = sys.stdin.readline
string = input().strip()
st = []
ppap = ["P","P","A","P"]

for s in string:
    st.append(s)
    if len(st) >= 4 and st[-4:] == ppap:
        st[-4:] = ["P"]
print("PPAP" if st == ["P"] else "NP")