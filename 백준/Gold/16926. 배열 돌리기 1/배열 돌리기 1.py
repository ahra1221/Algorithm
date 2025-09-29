import sys
input = sys.stdin.readline
n,m,r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
box = min(n,m) // 2

def set_layer(r, c, b):
    res = []
    for j in range(b, c - b):
        res.append((b, j))
    for i in range(b + 1, r - b - 1):
        res.append((i, c - b - 1))
    for j in range(c - b - 1, b - 1, -1):
        res.append((r - b - 1, j))
    for i in range(r - b - 2, b, -1):
        res.append((i, b))
    return res

for i in range(box):
    box_list = set_layer(n, m, i)
    vals = [arr[x][y] for x, y in box_list]
    rot = r % len(box_list)
    vals = vals[rot:] + vals[:rot]
    for (x,y), v in zip(box_list, vals):
        arr[x][y] = v
for i in range(n):
    print(" ".join(map(str, arr[i])))