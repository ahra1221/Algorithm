import sys

input = sys.stdin.readline
now = list(map(int, input().split(":")))
bomb = list(map(int, input().split(":")))
answer = []

for idx in range(2, -1, -1):
    n = now[idx]
    b = bomb[idx]
    if n <= b:
        answer.append(b-n)
    else:
        if idx == 0:
            b += 24
            answer.append(b-n)
        else:
            bomb[idx-1] -= 1
            b += 60
            answer.append(b-n)
out = [f'{x:02d}' for x in answer[::-1]]
if out == ['00','00','00']:
    print("24:00:00")
else:
    print(':'.join(out))