import sys

input = sys.stdin.readline
L,C = map(int, input().split())
word = list(input().split())
word.sort()

vo = {'a','e','i','o','u'}

answer = []

def dfs(st, cur):
    if len(cur) == L:
        a, b = 0, 0
        for c in cur:
            if c in vo: a += 1
            else: b += 1
        if a >= 1 and b >= 2: answer.append("".join(cur))
        return
    
    for i in range(st, C):
        cur.append(word[i])
        dfs(i+1, cur)
        cur.pop()

dfs(0,[])
for a in answer: print(a)