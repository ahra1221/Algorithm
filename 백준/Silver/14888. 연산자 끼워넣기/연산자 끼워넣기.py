import sys

input = sys.stdin.readline

max_result = - int(1e9)
min_result = int(1e9)


def backtracking(plus, minus, multiple, division, sum, idx):
    global max_result, min_result
    if idx == n:
        max_result = max(max_result, sum)
        min_result = min(min_result, sum)
        return
    if plus:
        backtracking(plus - 1, minus, multiple, division, sum + number[idx], idx + 1)
    if minus:
        backtracking(plus, minus - 1, multiple, division, sum - number[idx], idx + 1)
    if multiple:
        backtracking(plus, minus, multiple - 1, division, sum * number[idx], idx + 1)
    if division:
        backtracking(plus, minus, multiple, division - 1, int(sum / number[idx]), idx + 1)


n = int(input())
number = list(map(int, input().split()))
plus, minus, multiple, division = map(int, input().split())
backtracking(plus, minus, multiple, division, number[0], 1)
print(max_result)
print(min_result)