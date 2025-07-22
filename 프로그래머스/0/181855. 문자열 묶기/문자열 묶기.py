def solution(strArr):
    answer = [0] * len(strArr)
    for st in strArr:
        answer[len(st)] += 1
    return sorted(answer)[-1]