from bisect import bisect_left, bisect_right

n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
test = list(map(int, input().split()))


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

for i in range(len(test)):
    print(count_by_range(card, test[i], test[i]), end=' ')