def solution(order):
    answer = 0
    for ord in order:
        if "cafelatte" in ord:
            answer += 5000
        else:
            answer += 4500
    return answer