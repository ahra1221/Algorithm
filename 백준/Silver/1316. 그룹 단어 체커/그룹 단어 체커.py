import sys
import sys

input = sys.stdin.readline
N = int(input())
ans = 0

def check_group(word):
    g = {word[0]}
    for i in range(1, len(word)):
        if word[i] in g:
            if word[i-1] == word[i]: ## 연속중
                continue 
            else:
                return False
        else:
            g.add(word[i])
    return True

for _ in range(N):
    str = input().strip()
    if check_group(str):
        ans += 1

print(ans)