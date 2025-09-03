import sys

input = sys.stdin.readline
N = int(input())
postfix = input().strip()
nums = [int(input()) for _ in range(N)]
tmp = []

for se in postfix:
    if ord(se) >= 65:
        idx = ord(se) - ord('A')
        tmp.append(nums[idx])
    else:
        num2 = tmp.pop()
        num1 = tmp.pop()
        cal = eval(f'{num1}{se}{num2}')
        tmp.append(cal)

print("%.2f" %tmp[0])