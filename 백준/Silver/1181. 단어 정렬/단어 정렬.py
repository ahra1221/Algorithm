import sys

input = sys.stdin.readline

n = int(input())
words = []

for _ in range(n):
    word = input().strip()
    words.append(word)

words = list(set(words))
words.sort()
words.sort(key=len)

for i in words:
    print(i)
