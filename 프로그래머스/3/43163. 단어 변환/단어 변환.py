from collections import defaultdict, deque

def one_diff(w1,w2):
    diff = 0
    for idx in range(len(w1)):
        if w1[idx] != w2[idx]:
            diff += 1
    if diff == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 0
    
    visited = [False] * (len(words))
    q = deque()
    q.append((begin,0))
    while q:
        cur, dist = q.popleft()
        
        if cur == target:
            answer = dist
            break
        
        for i in range(len(words)):
            if not visited[i] and one_diff(words[i], cur):
                q.append((words[i], dist+1))
                visited[i] = True
   
    return answer