import itertools

array = [int(input()) for _ in range(9)]

for i in itertools.combinations(array, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break
        