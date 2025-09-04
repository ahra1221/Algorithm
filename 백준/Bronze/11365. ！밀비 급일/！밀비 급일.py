import sys

input = sys.stdin.readline

while True:
    password = input().strip()
    if password == 'END':
        break
    else:
        print(password[::-1])