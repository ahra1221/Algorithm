import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    string = input().strip()
    cnt = 0
    k = 0
    for i in string:
        if i == "O":
            k += 1
        else:
            k = 0
        cnt += k
    print(cnt)

