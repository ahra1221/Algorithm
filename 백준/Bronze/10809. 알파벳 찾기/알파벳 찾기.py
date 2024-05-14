import sys

input = sys.stdin.readline

s = input()
alpahbet = 'abcdefghijklmnopqrstuvwxyz'

for i in alpahbet:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print('-1', end=' ')