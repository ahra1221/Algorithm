def solution(numbers):
    answer = set()
    
    def dfs(st, cur):
        if len(cur) == 2:
            answer.add(sum(cur))
            return
        
        for i in range(st, len(numbers)):
            cur.append(numbers[i])
            dfs(i+1,cur)
            cur.pop()
    
    dfs(0,[])
    return sorted(list(answer))