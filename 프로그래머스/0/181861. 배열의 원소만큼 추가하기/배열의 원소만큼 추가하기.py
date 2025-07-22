def solution(arr):
    answer = []
    for a in arr:
        for _ in range(a):
            answer.append(a)
    return answer