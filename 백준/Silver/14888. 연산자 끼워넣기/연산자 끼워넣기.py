import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_value = -float('inf')
min_value = float('inf')

def dfs(idx, cur):
    global plus, minus, mul, div, max_value, min_value
    if idx == n:
        max_value = max(max_value, cur)
        min_value = min(min_value, cur)
        return
    if plus > 0:
        plus -= 1
        dfs(idx+1, cur+a[idx])
        plus += 1
    if minus > 0:
        minus -= 1
        dfs(idx+1, cur-a[idx])
        minus += 1
    if mul > 0:
        mul -= 1
        dfs(idx+1, cur*a[idx])
        mul += 1
    if div > 0:
        div -= 1
        dfs(idx+1, int(cur / a[idx]))
        div += 1
dfs(1, a[0])
print(max_value)
print(min_value)