import sys

input = sys.stdin.readline
N = int(input())
files = {}
for _ in range(N):
    f = input().strip()
    tmp = f.split(".")[1]
    if tmp in files:
        files[tmp] += 1
    else:
        files[tmp] = 1

for d in sorted(files.items()):
    print(d[0], d[1], sep=" ")