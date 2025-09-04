import sys

input = sys.stdin.readline
words = []
for _ in range(5):
    st = input().strip()
    words.append(list(st))

ans = ''
n = max(len(w) for w in words)
for i in range(n):
    for j in range(5):
        if len(words[j])-1 < i:
            continue
        else:
            ans += words[j][i]
print(ans)