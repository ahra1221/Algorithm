import sys

input = sys.stdin.readline

N = int(input())
string = str(input())
result = 1


def findLong(idx):
    global result
    if idx == N:
        return
    findLong(idx + 1)
    if string[idx:idx + 8:1] == 'longlong':
        result += 1
        findLong(idx + 8)


findLong(0)
print(result)
