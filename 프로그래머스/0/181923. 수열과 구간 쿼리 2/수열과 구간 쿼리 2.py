def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        li = []
        for i in range(s, e+1):
            if arr[i] > k:
                li.append(arr[i])
        
        if li:
            answer.append(min(li))
        else:
            answer.append(-1)
    return answer