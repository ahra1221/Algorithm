import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    nums = sorted(list(map(int, input().split())))
    print(nums[0], nums[-1])