from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    for idx, p in enumerate(priorities):
        q.append((p, idx))
    
    max_val = max(x[0] for x in q)
    while q:
        if (q[0][0] < max_val):
            q.append(q.popleft())
        else:
            pop_val = q.popleft()
            answer += 1
            if pop_val[1] == location: break
            if q: max_val = max(x[0] for x in q)
        
    return answer