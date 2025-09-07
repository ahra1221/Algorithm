import sys

input = sys.stdin.readline
N = int(input())
ans = 0

def digit_sum(x):
    return sum(map(int, str(x)))

for i in range(1, N+1):
    if i + digit_sum(i) == N:
        ans = i
        break

print(ans)