def solution(a, b):
    answer = 0
    a = str(a)
    b = str(b)
    answer = a+b if a+b>b+a else b+a
    return int(answer)