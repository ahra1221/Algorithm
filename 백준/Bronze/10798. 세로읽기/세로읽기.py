import sys

input = sys.stdin.readline

words = [input().strip() for _ in range(5)]
answer = ''

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end='')
