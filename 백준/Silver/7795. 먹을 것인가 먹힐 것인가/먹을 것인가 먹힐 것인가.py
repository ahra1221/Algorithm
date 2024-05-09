import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    n_size = list(map(int,input().split()))
    m_size = list(map(int,input().split()))

    n_size.sort()
    m_size.sort()
    st = 0
    cnt = 0

    for i in range(n):
        while True:
            if st == m or n_size[i] <= m_size[st]:
                cnt += st
                break
            else:
                st += 1
    print(cnt)

