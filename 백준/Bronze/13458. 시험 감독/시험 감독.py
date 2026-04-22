import sys
import math

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B,C = map(int, input().split())
answer = 0

for a in A:
    if a <= B: answer += 1
    else:
        left = a - B
        answer += 1
        answer += math.ceil(left / C)
print(answer)