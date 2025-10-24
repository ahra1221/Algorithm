import sys

input = sys.stdin.readline
n,m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

st_white = "WBWBWBWB"
st_black = "BWBWBWBW"

ans = 64

def make_chess(r,c):
    ans = []
    for i in range(r, r+8):
        l = []
        for j in range(c,c+8):
            l.append(board[i][j])
        ans.append(l)
    return ans

def count_chess(ch):
    first = ch[0][0]
    patterns = [st_white, st_black] if first == "W" else [st_black, st_white]
    cnt = 0
    for i, row in enumerate(ch):
        target = "".join(row)
        compare_to = patterns[i % 2]
        cnt += sum(c1 != c2 for c1, c2 in zip(target, compare_to))
    return min(cnt, 64 - cnt) 

for i in range(n-8+1):
    for j in range(m-8+1):
        chess = make_chess(i,j)
        ans = min(ans, count_chess(chess))

print(ans)
