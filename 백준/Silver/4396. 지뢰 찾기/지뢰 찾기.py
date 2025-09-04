import sys

input = sys.stdin.readline
n = int(input())
map = [input().strip() for _ in range(n)]
steps = [input().strip() for _ in range(n)]
ans = []
boom = False

def check(row, col):
    cnt = 0
    for i in range(max(0, row-1), min(n-1, row+1)+1):
        for j in range(max(0, col-1), min(n-1, col+1)+1):
            if i == row and j == col:
                continue
            if map[i][j] == "*":
                cnt += 1
    return cnt
    

for idx, step in enumerate(steps):
    tmp = ''
    for i, s in enumerate(step):
        if s == ".":
            tmp += "."
        else:
            if map[idx][i] == '*':
                boom = True
                tmp += "."
            else:
                tmp += str(check(idx, i))
    ans.append(tmp)

if boom:
    for r in range(n):
        row = list(ans[r])
        for c in range(n):
            if map[r][c] == '*':
                row[c] = '*'
        ans[r] = ''.join(row)
print(*ans, sep="\n")