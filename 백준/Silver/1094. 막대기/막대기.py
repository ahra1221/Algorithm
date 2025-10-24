import sys

input = sys.stdin.readline
x = int(input())
stick = [64]

while sum(stick) != x:
    small = stick.pop()
    half = small // 2
    stick.append(half)
    if sum(stick) < x:
        stick.append(half)
print(len(stick))