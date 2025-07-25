def solution(arr):
    row = len(arr)
    col = len(arr[0])
    if row > col:
        for a in arr:
            a += [0] * (row - col)
    else:
        arr += [[0] * col] * (col - row)
    return arr