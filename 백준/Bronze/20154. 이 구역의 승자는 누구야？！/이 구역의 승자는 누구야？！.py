import sys

input = sys.stdin.readline
K = input().strip()
line = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
tmp = []

for k in K:
    tmp.append(line[ord(k)- 65])
    if len(tmp) == 2:
        num1 = tmp.pop()
        num2 = tmp.pop()
        tmp.append((num1 + num2)% 10)
print("I'm a winner!" if tmp.pop() % 2 != 0 else "You're the winner?")