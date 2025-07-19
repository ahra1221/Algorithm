def solution(arr):
    answer = []
    tmp = list(filter(lambda x: arr[x] == 2, range(len(arr))))
    if len(tmp) == 0:
        return [-1]
    elif len(tmp) == 1:
        return [2]
    else:
        return arr[tmp[0]: tmp[-1]+1]
    return answer