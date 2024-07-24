def solution(strings, n):
    answer = []
    strings = sorted(strings, key=lambda x : x)
    answer = sorted(strings, key=lambda x : x[n])
    return answer