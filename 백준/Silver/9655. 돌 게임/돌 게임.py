import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1
if n == 1:
    print("SK")
    sys.exit(0)
else:
    n -= 2
ans = 0
while n > 0:
    if n >=3:
        n -= 3
    else:
        n -= 1
    ans += 1
print("CY" if not ans % 2 else "SK")