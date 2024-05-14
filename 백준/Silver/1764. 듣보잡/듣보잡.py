import sys

input = sys.stdin.readline

n, m = map(int, input().split())
no_listen = [input().strip() for _ in range(n)]
no_see = [input().strip() for _ in range(m)]

no_listen_see = sorted(list(set(no_listen) & set(no_see)))

print(len(no_listen_see))
for i in no_listen_see:
    print(i)
