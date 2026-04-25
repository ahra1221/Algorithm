import sys

input = sys.stdin.readline
r,c,k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

answer = 0
time = 0

while time <= 100:
    n,m = len(A), len(A[0])
    if r <= n and c <= m:
        if A[r-1][c-1] == k:
            print(answer)
            break
        
    if time == 100:
        print(-1)
        break
    newA = []
    
    if n >= m: #R연산
        for i in range(n):
            d = dict()
            for j in range(m):
                if A[i][j] > 0:
                    d[A[i][j]] = d.get(A[i][j], 0) + 1
            sorted_list = sorted(d.items(), key=lambda x: (x[1], x[0]))
            newr = []
            for num, cnt in sorted_list:
                newr.append(num)
                newr.append(cnt)
            newA.append(newr)
        
        max_len = max(len(row) for row in newA)
        for row in newA:
            row += [0] * min(max_len - len(row), 100)
        
        A = newA
        
    else: #C연산
        for j in range(m):
            d = dict()
            for i in range(n):
                if A[i][j] > 0:
                    d[A[i][j]] = d.get(A[i][j], 0) + 1
            sorted_list = sorted(d.items(), key=lambda x: (x[1], x[0]))
            
            newc = []
            for num, cnt in sorted_list:
                newc.append(num)
                newc.append(cnt)
            newA.append(newc)
        
        max_len = max(len(col) for col in newA)
        for col in newA:
            col += [0] * (max_len - len(col))
        
        tmp = []
        for i in range(min(max_len, 100)):
            arr = []
            for j in range(min(100,len(newA))):
                arr.append(newA[j][i])
            tmp.append(arr)
        A = tmp  
    answer += 1
    time += 1