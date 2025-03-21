def solution(x, y, n):
    answer = 0
    s = set()
    s.add(x)
    
    while s:
        if y in s:
            return answer
        nx = set()
        for i in s:
            if i+n <= y:
                nx.add(i+n)
            if i*2 <= y:
                nx.add(i*2)
            if i*3 <= y:
                nx.add(i*3)
        s = nx
        answer += 1
    
    return -1