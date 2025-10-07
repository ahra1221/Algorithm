def solution(a, b, n):
    answer = 0
    while n >= a:
        get = (n // a) * b
        answer += get
        n = get + n % a
    return answer