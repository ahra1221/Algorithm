import heapq

def solution(operations):
    answer = []
    q = []
    
    for opers in operations:
        oper, num = opers.split()
        num = int(num)
        
        if oper == 'I':
            heapq.heappush(q, num)
        elif oper == 'D' and num == 1:
            if len(q) != 0:
                max_value = max(q)
                q.remove(max_value)
        else:
            if len(q) != 0:
                heapq.heappop(q)
                              
    if len(q) == 0:
        answer = [0, 0]
    else:
        answer = [max(q), heapq.heappop(q)]
    return answer