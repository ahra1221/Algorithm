
N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
check_card = list(map(int, input().split()))


answer = []

for i in check_card:
    left, right = 0, len(cards) - 1
    hasValue = False
    while left <= right:
        mid = int((left + right) / 2)
        if cards[mid] < i:
            left = mid + 1
        elif cards[mid] > i:
            right = mid - 1
        else:
            hasValue = True
            break
    answer.append('1' if hasValue else '0')

print(" ".join(answer))
