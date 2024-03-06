import sys

input = sys.stdin.readline

n = int(input())
distance = []

for _ in range(n):
    a, b = map(int, input().split())
    distance.append([a, b])

result_x = sorted(distance, key=lambda x: x[0])[n // 2][0]
result_y = sorted(distance, key=lambda x: x[1])[n // 2][1]

sum = 0
for i in distance:
    sum += (abs(result_x - i[0]) + abs(result_y - i[1]))

print(sum)
