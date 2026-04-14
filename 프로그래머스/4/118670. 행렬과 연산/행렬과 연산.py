from collections import deque

def solution(rc, operations):
    answer = []
    
    left = deque()
    right = deque()
    mid = deque()
    
    n = len(rc)
    m = len(rc[0])
    
    for i in range(n):
        left.append(rc[i][0])
        right.append(rc[i][m-1])
        
        tmp = deque()
        for j in range(1, m-1):
            tmp.append(rc[i][j])
        mid.append(tmp)
    
    for op in operations:
        if op == "ShiftRow":
            left.appendleft(left.pop())
            right.appendleft(right.pop())
            mid.appendleft(mid.pop())
        else:
            mid[0].appendleft(left.popleft())
            right.appendleft(mid[0].pop())
            mid[n-1].append(right.pop())
            left.append(mid[n-1].popleft())
    
    for i in range(n):
        tmp = []
        tmp.append(left.popleft())
        while mid[i]: tmp.append(mid[i].popleft())
        tmp.append(right.popleft())
        answer.append(tmp)
    
    return answer