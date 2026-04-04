from collections import defaultdict

def solution(orders, course):
    answer = []
    ord = [list(o) for o in orders]
    
    for c in course:
        dic = defaultdict(int)
        
        for o in ord:
            def backtracking(idx, curr):
                if len(curr) == c:
                    dic["".join(sorted(curr))] += 1
                    return
            
                for i in range(idx, len(o)):
                    if o[i] not in curr:
                        curr.append(o[i])
                        backtracking(i+1, curr)
                        curr.pop()
            if len(o) >= c:
                backtracking(0, [])
        
        max_value = max(dic.values(), default=0)
        for k,v in dic.items():
            if v == max_value and v >= 2:
                answer.append(k)
    return sorted(answer)