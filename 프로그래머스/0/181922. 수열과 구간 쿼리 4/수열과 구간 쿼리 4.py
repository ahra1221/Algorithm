def solution(arr, queries):
    for s,e,k in queries:
        for i in range(s,e+1):
            if not(i % k):
                arr[i] += 1
    return arr