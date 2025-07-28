def solution(arr, k):
    answer = []
    for i in arr:
        if not i in answer:
            answer.append(i)
        if len(answer) == k:
            break
    answer += [-1] * (k-len(answer))
    return answer