import sys
input = sys.stdin.readline
p = int(input())
for _ in range(p):
    testcase = list(map(int, input().split()))
    t = testcase[0]
    arr = testcase[1:]

    ans = 0
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] > arr[i]:
                ans += 1
    print(f"{t} {ans}")