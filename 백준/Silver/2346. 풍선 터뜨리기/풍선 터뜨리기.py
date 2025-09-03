import sys

input = sys.stdin.readline
N = int(input())
moves = list(map(int, input().split()))
arr = [(i+1, mv) for i, mv in enumerate(moves)]
ans = []
cur = 0

for _ in range(N):
    idx, move = arr.pop(cur)
    ans.append(idx)
    if not arr: break

    if move > 0:
        cur = (cur + move - 1) % len(arr)
    else:
        cur = (cur + move) % len(arr)

print(*ans)