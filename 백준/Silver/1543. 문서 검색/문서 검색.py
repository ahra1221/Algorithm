import sys

input = sys.stdin.readline

docs = str(input().strip())
word = str(input().strip())
cnt = 0
i = 0

while i < len(docs) - len(word)  + 1:
    if docs[i:i+len(word)] == word:
        cnt += 1
        i += len(word)
    else:
        i += 1
print(cnt)


