def solution(numbers):
    answer = 0
    candidate = set()
    
    def backtracking(cur, t):
        if len(cur) == t:
            val = ''
            for c in cur:
                val += numbers[c]
            candidate.add(int(val))
            return
        
        for idx in range(len(numbers)):
            if idx not in cur:
                cur.append(idx)
                backtracking(cur, t)
                cur.pop()
    
    for target in range(1, len(numbers)+1):
        backtracking([], target)
    
    def isPrime(n):
        if n<2: return False
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
    
    for c in candidate:
        if isPrime(c): 
            answer += 1
    
    return answer