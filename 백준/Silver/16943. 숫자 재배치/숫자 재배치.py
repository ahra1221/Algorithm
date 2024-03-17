import sys
from itertools import permutations

input = sys.stdin.readline

a, b = map(str, input().split())
b = int(b)
answer = -1
a_list = ["".join(item) for item in permutations(a)]

for i in a_list:
    if i[0] == "0":
        continue
    i = int(i)
    if i < b:
        answer = max(answer, i)
print(answer)
