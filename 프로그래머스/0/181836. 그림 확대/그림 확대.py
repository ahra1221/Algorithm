def solution(picture, k):
    answer = []
    for idx, pic in enumerate(picture):
        tmp = ''
        for p in pic:
            tmp += p*k
        answer += [tmp] * k
    return answer