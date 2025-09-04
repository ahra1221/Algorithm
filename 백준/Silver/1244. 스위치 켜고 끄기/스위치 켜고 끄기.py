import sys

input = sys.stdin.readline
N = int(input())
switchs = list(map(int, input().split()))
students = int(input())
for st in range(students):
    gender, number = map(int, input().split())
    if gender == 1:
        for i in range(number, N+1, number):
            switchs[i-1] = int(not bool(switchs[i-1]))
    else:
        switchs[number-1] = int(not bool(switchs[number-1]))
        for i in range(min(number-1, N-number)):
            if switchs[number-i-2] == switchs[number+i]:
                switchs[number-i-2] = int(not bool(switchs[number+i]))
                switchs[number+i] = int(not bool(switchs[number+i]))
            else:
                break

for i in range(0, len(switchs), 20):
    print(*switchs[i:i+20])