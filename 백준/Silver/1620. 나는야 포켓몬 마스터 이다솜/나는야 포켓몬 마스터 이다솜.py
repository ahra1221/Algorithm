import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d = dict()
for i in range(n):
    pokemon = input().strip()
    d[i+1] = pokemon
revd = {v:k for k,v in d.items()}
for _ in range(m):
    quiz = input().strip()
    if quiz.isdigit():
        print(d[int(quiz)])
    else:
        print(revd[quiz])