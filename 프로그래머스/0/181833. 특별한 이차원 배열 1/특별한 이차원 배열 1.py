def solution(n):
    answer = []
    for i in range(n):
        tmp = []
        for j in range(n):
            if i == j:
                tmp.append(1)
            else:
                tmp.append(0)
        answer.append(tmp)
    return answer