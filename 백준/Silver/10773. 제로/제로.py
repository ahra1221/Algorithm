count = int(input())
money = []

for i in range(count):
    num = int(input())
    if num == 0:
        money.pop()
    else:
        money.append(num)
print(sum(money))