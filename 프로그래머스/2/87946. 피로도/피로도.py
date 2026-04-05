def solution(k, dungeons):
    answer = 0
    
    def backtracking(now, curr):
        nonlocal answer
        answer = max(answer, len(curr))
        
        for idx in range(len(dungeons)):
            a,b = dungeons[idx]
            if a <= now and idx not in curr:
                curr.append(idx)
                backtracking(now-b, curr)
                curr.pop()
    backtracking(k, [])
    return answer