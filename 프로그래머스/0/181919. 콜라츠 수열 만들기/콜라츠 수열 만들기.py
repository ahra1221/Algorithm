def solution(n):
    answer = [n]
    while n > 1:
        n = n/2 if not(n%2) else 3*n+1
        answer.append(n)
    return answer