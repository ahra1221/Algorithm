def solution(arr, flag):
    answer = []
    for idx, f in enumerate(flag):
        if f:
            answer += [arr[idx]] * arr[idx] * 2
        else:
            del answer[len(answer)-arr[idx]:]
    return answer