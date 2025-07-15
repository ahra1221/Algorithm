def solution(a, d, included):
    answer = 0
    for idx, i in enumerate(included):
        if i:
            answer += a + d * idx
    return answer