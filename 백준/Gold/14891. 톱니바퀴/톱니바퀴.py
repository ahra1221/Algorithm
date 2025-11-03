import sys

input = sys.stdin.readline
wheel = [list(map(int, input().strip())) for _ in range(4)]
k = int(input())
ans = 0

def rotate_wheel(wheel, isClock):
    if isClock:
        return [wheel[-1]]+wheel[:-1]
    else:
        return wheel[1:]+[wheel[0]]

for _ in range(k):
    num, dir = map(int, input().split())
    num -= 1
    rotate = [0,0,0,0]
    rotate[num] = dir
    
    for i in range(num-1, -1, -1):
        if wheel[i][2] != wheel[i+1][6]:
            rotate[i] = -rotate[i+1]
        else:
            break
    for i in range(num+1, 4):
        if wheel[i][6] != wheel[i-1][2]:
            rotate[i] = -rotate[i-1]
        else:
            break
    for i in range(4):
        if rotate[i] == 1:
            wheel[i] = rotate_wheel(wheel[i], True)
        elif rotate[i] == -1:
            wheel[i] = rotate_wheel(wheel[i], False)

for i in range(4):
    if wheel[i][0] == 1:
        ans += 2 ** i
print(ans)