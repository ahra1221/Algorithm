import sys

input = sys.stdin.readline

n = int(input())

for i in range(1, 10, 1):
    print("%d * %d = %d" % (n, i, n * i))
