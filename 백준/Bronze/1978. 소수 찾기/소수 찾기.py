import sys
import math

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
cnt = 0


def is_prime_number(x):
    for j in range(2, x):
        if x % j == 0:
            return False
    return True


for i in numbers:
    if i > 1 & is_prime_number(i) == True:
        cnt += 1

print(cnt)
