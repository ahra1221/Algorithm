def solution(a, b):
    answer = 0
    if a % 2 and b % 2:
        return a**2+b**2
    elif not(a % 2 or b % 2):
        return abs(a-b)
    else:
        return 2 * (a+b)
    return answer