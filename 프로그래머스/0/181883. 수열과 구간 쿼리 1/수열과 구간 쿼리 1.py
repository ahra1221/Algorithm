def solution(arr, queries):
    for st, en in queries:
        for idx in range(st, en+1):
            arr[idx] += 1
    return arr