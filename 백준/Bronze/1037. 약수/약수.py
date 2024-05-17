import sys

input = sys.stdin.readline

n = int(input())
real_num = list(map(int, input().split()))
real_num.sort()
print(real_num[0] * real_num[n-1])
