def solution(arr, intervals):
    answer = []
    for st, en in intervals:
        for a in arr[st:en+1]:
            answer.append(a)
    return answer