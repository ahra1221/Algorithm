import sys
input = sys.stdin.readline

n, taesu, p = map(int, input().split())
scores = list(map(int, input().split()))

if n == 0:
    print(1)
elif n == p and taesu <= scores[-1]:
    print(-1)
else:
    rank = 1
    for s in scores:
        if s <= taesu:
            break
        else:
            rank += 1
    print(rank)