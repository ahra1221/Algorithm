import sys

input = sys.stdin.readline


def backtracking(start):
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(start, n + 1):
        if i not in arr:
            arr.append(i)
            backtracking(i+1)
            arr.pop()


n, m = map(int, input().split())
arr = []
backtracking(1)
