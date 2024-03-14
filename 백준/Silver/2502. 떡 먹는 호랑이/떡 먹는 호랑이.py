import sys

input = sys.stdin.readline

D, K = map(int, input().split())

a, b = 1, 1
for _ in range(2, D - 1):
    a, b = b, a + b

answer_a = 1
answer_b = 0

while True:
    tmp = K - a * answer_a
    if tmp % b == 0:
        answer_b = tmp // b
        break
    answer_a += 1

print(answer_a)
print(answer_b)
