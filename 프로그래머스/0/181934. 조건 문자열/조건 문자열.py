def solution(ineq, eq, n, m):
    answer = 0
    if (ineq, eq)  == (">", "="):
        answer = n >= m
    elif (ineq, eq)  == ("<", "="):
        answer = n <= m
    elif (ineq, eq)  == (">", "!"):
        answer = n > m
    elif (ineq, eq)  == ("<", "!"):
        answer = n < m
    return int(answer)