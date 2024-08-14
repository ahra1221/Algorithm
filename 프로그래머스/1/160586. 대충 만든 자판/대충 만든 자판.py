def solution(keymap, targets):
    answer = []
    dic = {}
    
    for row in keymap:
        for idx, char in enumerate(row):
            if char in dic:
                dic[char] = min(dic[char], idx + 1)
            else:
                dic[char] = idx + 1
                
    for target in targets:
        ans = 0
        for char in target:
            if char in dic:
                ans += dic[char]
            else:
                ans = -1
                break
        answer.append(ans)
        
    return answer