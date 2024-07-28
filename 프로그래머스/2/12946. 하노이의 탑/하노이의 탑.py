def solution(n):
    answer = []
    
    def hanoi(n, st, mid, end):
        if n == 1:
            answer.append([st, end])
        else:
            hanoi(n-1, st, end, mid)
            hanoi(1, st, mid, end)
            hanoi(n-1, mid, st, end)
            
    hanoi(n, 1, 2, 3)
    return answer