numbers = list(range(1, 10_001))
removeNumbers = list()

for num in numbers:
    for n in str(num):
        num += int(n)
    if num <= 10000:
        removeNumbers.append(num)

for removeNum in set(removeNumbers):
    numbers.remove(removeNum)

for selfNum in numbers:
    print(selfNum)