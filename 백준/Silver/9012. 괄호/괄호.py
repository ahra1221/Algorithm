import sys

input = sys.stdin.readline

def is_vps(str):
    stack = []
    for st in str:
        if st == "(":
            stack.append(st)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
    return not stack

N = int(input())

for _ in range(N):
    testcase = input().strip()
    print("YES" if is_vps(testcase) else "NO")
