def solution(arr, idx):
    answer = 0
    arr = arr[idx:]
    try:
	    answer = arr.index(1) + idx
    except ValueError:
        answer = -1
    return answer