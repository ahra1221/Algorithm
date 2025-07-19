def solution(arr, query):
    for idx, q in enumerate(query):
        if not(idx % 2):
            arr = arr[:q+1]
        else:
            arr = arr[q:]
    return arr