import sys

input = sys.stdin.readline


def backtracking(st):
    if len(arr) == m:
        print(" ".join(map(str, arr)))
        return
    for i in range(st, n + 1):
        arr.append(i)
        backtracking(i)
        arr.pop()


n, m = map(int, input().split())
arr = []
backtracking(1)