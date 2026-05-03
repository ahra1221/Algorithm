def solution(word):
    answer = 0
    dic = ['A', 'E', 'I', 'O', 'U']
    found = False
    
    def dfs(cur):
        nonlocal answer, found
        if found: return
        if cur != "":
            answer += 1
            if cur == word:
                found = True
                return
        
        if len(cur) == 5: return
    
        for d in dic:
            dfs(cur + d)
        
    dfs("")
    return answer