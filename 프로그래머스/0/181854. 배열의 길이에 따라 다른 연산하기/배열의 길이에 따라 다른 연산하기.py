def solution(arr, n):
    answer = []
    if not(len(arr) % 2):
        for idx in range(1, len(arr) + 1, 2):
            arr[idx] += n
    else:
        for idx in range(0, len(arr) + 1, 2):
            arr[idx] += n    
    return arr