import math

num = int(input())

for i in range(num):
    num1, num2 = map(int, input().split())
    print(math.lcm(num1, num2))