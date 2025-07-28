def solution(arr):
    tmp = 0
    while True:
        if 2 ** tmp - len(arr) >= 0:
            break
        else:
            tmp += 1
    arr += [0] * (2 ** tmp - len(arr))
    return arr