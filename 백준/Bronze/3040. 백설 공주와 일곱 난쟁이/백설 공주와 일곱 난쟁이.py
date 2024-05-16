import sys
from itertools import combinations

input = sys.stdin.readline

num = [int(input()) for _ in range(9)]
case = list(combinations(num, 7))

for i in case:
    if sum(i) == 100:
        for j in i:
            print(j)

