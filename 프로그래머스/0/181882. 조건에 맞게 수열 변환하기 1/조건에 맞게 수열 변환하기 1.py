def solution(arr):
    for idx, a in enumerate(arr):
        if a >= 50 and not(a % 2):
            arr[idx] = a / 2
        elif a < 50 and a % 2 != 0:
            arr[idx] = a * 2
    return arr