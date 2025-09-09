import sys

input = sys.stdin.readline
N = int(input())
num = int(input())
candidate = list(map(int, input().split()))
picture = {}

def find_pop(p):
    return min(p, key=lambda s: (p[s][0], p[s][1]))

for idx, c in enumerate(candidate):
    if c in picture:
        cnt, t = picture[c]
        picture[c] = (cnt +1, t)
    else:
        if len(picture) < N:
            picture[c] = (1, idx)
        else:
            picture.pop(find_pop(picture))
            picture[c] = (1, idx)

print(" ".join(map(str, sorted(picture.keys()))))