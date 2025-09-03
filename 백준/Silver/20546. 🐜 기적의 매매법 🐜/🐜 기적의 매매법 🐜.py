import sys

input = sys.stdin.readline
total = int(input())
money = list(map(int, input().split()))

def jun(total, moneys):
    buy = 0
    for money in moneys:
        if money <= total:
            buy += total // money
            total %= money
        if total == 0:
            break
    return (buy, total)

def sung(total, moneys):
    high = 0
    low = 0
    buy = 0
    for idx, money in enumerate(moneys):
        if moneys[idx-1] < money:
            low = 0
            high += 1
        elif moneys[idx-1] > money:
            high = 0
            low += 1
        if high >= 3 and buy >= 0:
            total += buy * money
            buy = 0
        elif low >= 3 and total > 0:
            buy += total // money
            total %= money
    return (buy, total)

a = jun(total=total, moneys=money)
b = sung(total=total, moneys=money)
aj = a[1] + a[0] * money[-1]
bs = b[1] + b[0] * money[-1]
if aj == bs:
    print("SAMESAME")
elif aj > bs:
    print("BNP")
else:
    print("TIMING")