import sys

input = sys.stdin.readline

string = str(input())
array = [[0] * 26 for _ in range(len(string) + 1)]

for i in range(1, len(string)+1):
    for j in range(26):
        if ord(string[i-1])-97 == j:
            array[i][j] = array[i-1][j] + 1
        else:
            array[i][j] = array[i-1][j]

q = int(input())

for _ in range(q):
    a, l, r = input().split()
    a, l, r = ord(a)-97, int(l), int(r)
    print(array[r+1][a]-array[l][a])

